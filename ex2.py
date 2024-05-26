import json
from pykma.KMA import KMA
from pykma.links import *

myKma = KMA("your API key")

typ01_to_json = myKma.typ01_request(ASOS_SPECIFIC_TIME_REQUEST)

# 파일에 작성
with open("station_info2.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(typ01_to_json.to_json(), indent=4, ensure_ascii=False))