# 기상청 API 전용 파이썬 모듈

## 개요

기상청에서는 [OpenAPI 서비스](https://apihub.kma.go.kr/)를 제공하고 있다. 그러나, 모든 API의 호출 타입이 json 혹은 xml로 이루어져있지 않다. 특히, 가장 많이 사용할 것으로 예상되는 ASOS(종관관측), AWS(방재관측) API의 대부분은 일반 텍스트로 이루어져있다. 이는 파이썬에서 활용하기 다소 까다롭게 만든다. 

우선, 기상청 API URL에 적혀있는 `typ`라는 요소에 대해 알아야 한다. 조사한 바로는 다음과 같다.

| Name | Real Type | Remark |
| --- | --- | --- |
| typ01 | csv 형식 (띄어쓰기로 구분됨) | |
| typ02 | XML 혹은 JSON | |
| typ03 | 이미지 |
| typ04 | 레이더 nc 파일 | 웹 미리보기 안 됨. |
| typ05 | 위성 nc 파일 | 웹 미리보기 안 됨. |
| typ06 | gb2 파일 | 웹 미리보기 안 됨. |
| typ07 | 수치모델 그래픽 | |
| typ08 | JSON | 산악 날씨 데이터 |
| typ09 | .xml, .xls 파일 | 웹 미리보기 안 됨. |

여기서 ASOS, AWS 등은 typ01형 데이터를 제공하고 있다. 이 라이브러리는 기존 typ01을 요청할 때, text를 변환해 마치 json 객체처럼 동작할 수 있도록 편리하게 변환하는 기능을 제공하고자 한다.

구현의 어려운 점은 text 형으로 이루어져있는 표의 비일관성이다. `help` 파라미터를 넣지 않고 호출할 경우 표의 내용을 한눈에 알아보기 어려우며, 또한 표의 머리표(헤더)가 두 줄로 이루어져있어 단위 변환 등의 과정이 까다롭다. 이 때문에 `help` 파라미터는 의무적으로 삽입해야하는 요소이며, 이는 어쩔 수 없이 typ01 데이터 호출의 자율성을 약간 감소시키는 문제점이 있다. 그래도 기존 표와는 다르게 사용자가 자유로히 사용하기 좋게 Json 구조화를 이뤘다.

## 사전 처리

우선 사용자는 [기상청 OpenAPI](https://apihub.kma.go.kr/)에서 회원가입 후 자신의 API 키를 발급받아야 한다. 그리고, 자신이 사용하고자 하는 API 서비스를 요청해야 한다. 

## 예제 코드

```python
import json
from pykma.KMA import KMA
from pykma.links import *

myKma = KMA("your API key")

# 사전에 지상관측 지점정보 API 활용신청 필요
typ01_to_json = myKma.typ01_request(STATION_INFO, {"inf": "AWS"})

# 파일에 작성
with open("station_info.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(typ01_to_json.to_json(), indent=4, ensure_ascii=False))
```

위의 경우 방재관측 측정소의 모든 정보를 호출해 json 파일로 저장하게끔 돕는다. 

실제 저장된 json 파일은 다음과 같을 것이다.

```json
{
    "header": [
        {
            "name": "STN_ID",
            "description": "지점번호"
        },
        ...
    ],
    "content": [
        {
            "STN_ID": 90,
            "LON": 128.56473,
            "STN_SP": 38.25085,
            "HT": 41211110,
            "HT_PA": 17.53,
            "HT_TA": 10.0,
            "HT_WD": 4111,
            "HT_RN": 105,
            "STN_CD": "속초",
            "STN_KO": null,
            "STN_EN": "11D20402",
            "STN_AD": 5182033035,
            "FCT_ID": 282
        },
        ...
    ]
}
```

## 클래스 구조

### `KMA`

전체 서비스를 시작할 때 선언해야하는 메인 클래스이다. 일반적인 경우 typ01 리퀘스트에 대해 다음 함수를 사용할 수 있다.

```python
def typ01_request(self, url: URLManager, attr=None)
```

그러나, 만약 자신이 직접 원하는 방향으로 데이터를 변환하고자 하거나, typ01이 아닌 리퀘스트에 대해 다음 함수를 사용할 수 있다.

```python
def custom_request(self, url: URLManager, attr:Attribute, func=lambda x: x)
```

이때, `func`은 전체 request 결과를 변형하는 wrapper 함수로, 인자로는 `Response` 타입의 객체를 받는다고 가정해야 한다.

예를 들어, `typ01_request`는 다음 func를 정의하고 `custom_request`를 호출한다.

```python
def toTable(req):
    if (req.status_code != 200):
        raise Exception("Error: " + str(req.status_code) + " " + req.json()["result"]["message"])
    myTable = Table(req.text)
    return myTable
```

### `Authorization`

단순히 사용자의 API Key를 담아두는 객체이다.

### `Attribute`

API URL의 쿼리 파라미터를 담아두는 객체이다. 메소드를 통해 파라미터를 저장할 수도 있고, 선언 시에 딕셔너리를 삽입해 사용할 수도 있다.

```python
Attribute({딕셔너리})
```

### `URLManager`

전체 URL 정보를 종합하고 서버에 단순히 API 요청을 보낼 수 있는 클래스이다. `URLManager`는 기본 url이 필요하다. 대부분의 서비스는 `pykma/links.py`에 저장되어 있다. 거기에 없다면 다음과 같이 호출해서 사용하면 된다.

```python
myLink = URLManager("원하는 링크", Attribute, Authorization)
```

이렇게 선언되면 다음과 같이 API 요청을 보낼 수 있다.

```python
myLink.request()
```

