import json
from pykma.KMA import KMA
from pykma.links import *

myKma = KMA("your API key")

typ01_to_json = myKma.typ01_request(STATION_INFO, {"inf": "AWS"})

# 파일에 작성
with open("station_info.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(typ01_to_json.to_json(), indent=4, ensure_ascii=False))