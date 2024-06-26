import re
from collections import OrderedDict # for Python 3.5 and earlier

def is_number(str):
    try:
        k = float(str)
        return k == k
    except ValueError:
        return False

class Table:
    def __init__(self, data_stream: str):
        self.data_stream = data_stream
        self.data = []
        self.header = OrderedDict()
        self._parse_data()
        
    def _parse_data(self):
        lines = self.data_stream.split('\n')
        for line in lines:
            if line.startswith('#'):
                match = re.match(r'^# *(\d*)\.* ([\w\d_]+) *: (.*)', line)
                if match:
                    _, col_name, description = match.groups()
                    self.header[col_name] = description
            else:
                parsed = line.split()
                for i, p in enumerate(parsed):
                    if is_number(p):
                        parsed[i] = float(p) if not p.isdigit() else int(p)
                    elif p.count('-') >= 2:
                        parsed[i] = None
                if len(parsed) == 0:
                    continue
                self.data.append(parsed)
                
    def get_headers(self) -> list:
        return self.header.keys()
    
    def get_header_dict(self) -> OrderedDict:
        return self.header
    
    def get_document(self, index: int) -> list:
        return self.data[index]
    
    def to_json(self) -> dict:
        result = OrderedDict()
        result["header"] = []
        for k, v in self.header.items():
            result["header"].append({"name": k, "description": v})
        result["content"] = []
        for d in self.data:
            result["content"].append(dict(zip(self.header.keys(), d)))
        return dict(result)
                
                
if __name__ == '__main__':
    data = """#START7777
#--------------------------------------------------------------------------------------------------
#  기상청 지상관측 시간자료 [입력인수형태][예] ?tm=201007151200&stn=0&help=1
#--------------------------------------------------------------------------------------------------
#  1. TM     : 관측시각 (KST)
#  2. STN    : 국내 지점번호
#  3. WD     : 풍향 (16방위)
#  4. WS     : 풍속 (m/s)
#  5. GST_WD : 돌풍향 (16방위)
#  6. GST_WS : 돌풍속 (m/s)
#  7. GST_TM : 돌풍속이 관측된 시각 (시분)
#  8. PA     : 현지기압 (hPa)
#  9. PS     : 해면기압 (hPa)
# 10. PT     : 기압변화경향 (Code 0200) 
# 11. PR     : 기압변화량 (hPa)
# 12. TA     : 기온 (C)
# 13. TD     : 이슬점온도 (C)
# 14. HM     : 상대습도 (%)
# 15. PV     : 수증기압 (hPa)
# 16. RN     : 강수량 (mm) : 여름철에는 1시간강수량, 겨울철에는 3시간강수량
# 17. RN_DAY : 일강수량 (mm) : 해당시간까지 관측된 양(통계표)
# 18. RN_JUN : 일강수량 (mm) : 해당시간까지 관측된 양을 전문으로 입력한 값(전문)
# 19. RN_INT : 강수강도 (mm/h) : 관측하는 곳이 별로 없음
# 20. SD_HR3 : 3시간 신적설 (cm) : 3시간 동안 내린 신적설의 높이
# 21. SD_DAY : 일 신적설 (cm) : 00시00분부터 위 관측시간까지 내린 신적설의 높이
# 22. SD_TOT : 적설 (cm) : 치우지 않고 그냥 계속 쌓이도록 놔눈 경우의 적설의 높이
# 23. WC     : GTS 현재일기 (Code 4677)
# 24. WP     : GTS 과거일기 (Code 4561) .. 3(황사),4(안개),5(가랑비),6(비),7(눈),8(소나기),9(뇌전)
# 25. WW     : 국내식 일기코드 (문자열 22개) : 2자리씩 11개까지 기록 가능 (코드는 기상자원과 문의)
# 26. CA_TOT : 전운량 (1/10)
# 27. CA_MID : 중하층운량 (1/10)
# 28. CH_MIN : 최저운고 (100m)
# 29. CT     : 운형 (문자열 8개) : 2자리 코드로 4개까지 기록 가능
# 30. CT_TOP : GTS 상층운형 (Code 0509)
# 31. CT_MID : GTS 중층운형 (Code 0515)
# 32. CT_LOW : GTS 하층운형 (Code 0513)
# 33. VS     : 시정 (10m)
# 34. SS     : 일조 (hr)
# 35. SI     : 일사 (MJ/m2)
# 36. ST_GD  : 지면상태 코드 (코드는 기상자원과 문의)
# 37. TS     : 지면온도 (C)
# 38. TE_005 : 5cm 지중온도 (C)
# 39. TE_01  : 10cm 지중온도 (C)
# 40. TE_02  : 20cm 지중온도 (C)
# 41. TE_03  : 30cm 지중온도 (C)
# 42. ST_SEA : 해면상태 코드 (코드는 기상자원과 문의)
# 43. WH     : 파고 (m) : 해안관측소에서 목측한 값
# 44. BF     : Beaufart 최대풍력(GTS코드)
# 45. IR     : 강수자료 유무 (Code 1819) .. 1(Sec1에 포함), 2(Sec3에 포함), 3(무강수), 4(결측)
# 46. IX     : 유인관측/무인관측 및 일기 포함여부 (code 1860) .. 1,2,3(유인) 4,5,6(무인) / 1,4(포함), 2,5(생략), 3,6(결측)
#--------------------------------------------------------------------------------------------------
#2345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234
# YYMMDDHHMI STN  WD   WS GST  GST  GST     PA     PS PT    PR    TA    TD    HM    PV     RN     RN     RN     RN     SD     SD     SD WC WP WW                      CA  CA   CH CT        CT  CT  CT    VS   SS    SI ST    TS    TE    TE    TE    TE  ST   WH BF IR IX
#        KST  ID  16  m/s  WD   WS   TM    hPa    hPa  -   hPa     C     C     %   hPa     mm    DAY    JUN    INT    HR3    DAY    TOT -- -- ---------------------- TOT MID  MIN -------- TOP MID LOW                  GD     C     5    10    20    30 SEA    m --  -  -
202211300900  90  29  4.6  32 10.0  331 1025.7 1028.0  2   1.7  -3.0 -24.6  17.0   0.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        2   0   -9 -         -9  -9  -9  5000  1.0 -9.00 -9  -1.0 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900  93  36  2.5  -9 -9.0   -9 1020.6 1033.1  2   2.7  -6.3 -21.4  29.0   1.1   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  2000  1.0  0.55 -9  -2.6   0.8   2.5   5.1   7.0  -9 -9.0 -9  3  2
202211300900  95  27  2.1  -9 -9.0   -9 1014.0 1034.4  2   2.5  -8.0 -19.2  40.0   1.3   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  5009  0.8  0.43 -9  -1.2 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900  98  34  1.8  -9 -9.0   -9 1019.2 1034.4  2   2.6  -6.9 -17.4  43.0   1.6   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  3335  0.7  0.43 -9  -2.3 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900  99  34  2.2  -9 -9.0   -9 1031.1 1035.1  2   2.6  -6.7 -16.4  46.0   1.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  4139  1.0  0.48 -9  -1.5 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 100  29  2.3  29 14.0  459  933.2 1030.3  2   3.8  -9.3 -23.7  30.0   0.9   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  5000  0.9  0.49 -9  -4.8 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 101  29  1.3  -9 -9.0   -9 1023.0 1032.9  2   2.8  -6.0 -19.7  33.0   1.3   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0  -9   -9 -         -9  -9  -9  5000  0.7  0.46 -9  -3.6   2.4   3.2   6.4   8.2  -9 -9.0 -9  3 -9
202211300900 102  34 11.9  34 20.0  312 1029.3 1034.0  2   2.0  -4.6  -9.0  71.0   3.1    0.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 70 77 05                       8   8    8 Sc         0   0   5  1854  0.0  0.08 -9  -5.0 -99.0 -99.0 -99.0 -99.0  -9  2.5 -9  1  1
202211300900 104  36  4.1  32 10.0  453 1017.6 1027.2  2   2.7  -1.2 -20.2  22.0   1.2   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  2000  0.9  0.57 -9  -0.3   2.6   4.7   9.1   9.7  -9 -9.0 -9  3  2
202211300900 105  32  2.7  -9 -9.0   -9 1024.4 1027.9  2   2.7  -0.8 -15.8  31.0   1.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        3   0   -9 -         -9  -9  -9  5000  0.8 -9.00 -9   0.3   3.7   5.5   7.5   9.4  -9 -9.0 -9  3  2
202211300900 106  32  3.3  -9 -9.0   -9 1022.6 1027.8  2   3.7   0.4 -18.9  22.0   1.4   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        2   0   -9 -         -9  -9  -9  4973  0.7 -9.00 -9  -0.9 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 108  27  4.1  -9 -9.0   -9 1022.3 1033.5  2   2.5  -6.6 -15.0  51.0   1.9   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  2000  1.0  0.47 -9  -2.2   4.8   5.5   7.4   9.5  -9 -9.0 -9  3  2
202211300900 112  32  6.0  32 14.0  537 1024.6 1033.6  2   2.4  -6.1 -15.6  47.0   1.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        1   1   10 Sc         0   0   5  3932  0.9  0.45 -9  -2.1   3.7   4.6   7.0   9.3   3  1.0  4  3  2
202211300900 114  32  2.0  -9 -9.0   -9 1013.5 1033.0  2   3.2  -4.6 -17.1  37.0   1.6   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  5000  1.0  0.60 -9  -1.1 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 115  11  3.4  36 22.0  719  995.2 1022.7  2   3.7   2.2  -3.7  65.0   4.6    0.0    1.0    1.0   -9.0   -9.0   -9.0   -9.0 70 72 05                       9   9   10 Sc         0   0   5  2865  0.0  0.18 -9   3.1   5.5   7.8  10.0  10.6   6  4.5  3  1  1
202211300900 119  32  3.8  -9 -9.0   -9 1028.8 1034.0  2   2.3  -6.3 -13.8  55.0   2.1   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  1991  1.0  0.49 -9  -1.0 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3  2
202211300900 121  27  3.1  -9 -9.0   -9 1000.4 1031.3  2   3.3  -4.1 -16.6  37.0   1.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  5000  0.8 -9.00 -9  -1.0 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 127  27  3.8  -9 -9.0   -9 1017.4 1032.3  2   3.0  -4.7 -18.2  34.0   1.5   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  4968  0.4  0.28 -9  -0.9 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 129  29  4.5  32 10.0  406 1030.4 1033.7  2   2.3  -3.5  -8.0  71.0   3.3    0.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   2   76 -         -9  -9  -9   519  0.0  0.18 -9   1.3   3.1   5.1   7.4   9.0  -9 -9.0 -9  1 -9
202211300900 130  27  2.3  -9 -9.0   -9 1021.3 1027.6  2   4.6  -0.3 -16.6  28.0   1.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        7   0   -9 -         -9  -9  -9  5000  0.0 -9.00 -9   1.2 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 131  29  2.3  -9 -9.0   -9 1025.6 1033.2  2   2.7  -3.5 -15.1  40.0   1.9   -9.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        1   0   -9 Ci         1   0   0  4977  0.7  0.34 -9  -0.2 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3  2
202211300900 133   2  4.0  34 14.0  305 1024.4 1033.5  2   2.6  -3.7 -13.6  46.0   2.1   -9.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        3   1   12 ScCi       1   0   5  4976  0.5  0.30 -9  -0.6   3.2   6.8   8.6  10.0  -9 -9.0 -9  3  2
202211300900 135  29  6.0  25 16.0  323 1000.1 1031.6  2   3.1  -5.0 -15.1  45.0   1.9   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  4820  0.0  0.25 -9  -4.2 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 136  29  4.6  29 11.0  826 1012.7 1030.9  2   3.6  -3.3 -16.9  34.0   1.6   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 Ci         2   0   0  5000  0.1  0.31 -9  -0.5 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3  2
202211300900 137  27  3.0  -9 -9.0   -9 1018.3 1030.8  2   3.1  -3.5 -20.2  26.0   1.2   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  5000  0.2  0.25 -9  -0.3 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 138  29  4.3  -9 -9.0   -9 1027.7 1028.2  2   3.6   0.6 -17.7  24.0   1.5   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   1   12 ScAs      -9   2   5  2000  0.0  0.24 -9   1.0   5.0   7.8  10.8  12.4   2  0.5  3  3  2
202211300900 140  32  2.2  34 11.0  420 1029.9 1033.5  2   2.0  -1.7  -9.3  56.0   3.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   8   10 -         -9  -9  -9  5000  0.1 -9.00 -9   0.0 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 143  25  6.0  25 11.0  857 1022.8 1029.8  3   3.6  -1.4 -14.5  36.0   2.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 Ci         2   0   0  2000  0.0  0.32 -9   2.0 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3  2
202211300900 146  36  3.2  -9 -9.0   -9 1024.9 1032.7  2   2.2  -1.9 -10.2  53.0   2.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   2   14 ScCi       1   0   5  2000  0.1  0.29 -9   2.1 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3  2
202211300900 152  36  2.5  -9 -9.0   -9 1016.5 1026.8  2   4.3   1.2 -18.2  22.0   1.5   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   0   -9 Ci         2   0   0  2000  0.6 -9.00 -9   3.8 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3  2
202211300900 155   7  2.5   5 13.0  421 1022.6 1027.1  2   2.9  -0.1 -13.4  36.0   2.2   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   0   -9 Ci         2   0   0  5000  0.4  0.44 -9   2.0 -99.0 -99.0 -99.0 -99.0   2  0.5  2  3  2
202211300900 156   5  3.8   5 10.0  426 1022.3 1031.3  2   2.5   0.5  -9.5  47.0   3.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   9   12 Sc         0   0   5  2000  0.3  0.49 -9   4.4 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3  2
202211300900 159  14  2.6  23 19.0  659 1016.7 1025.4  2   3.4   3.2 -14.0  27.0   2.1   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   0   -9 Ci         2   0   0  5000  0.2  0.45 -9   8.2   7.9  10.4  12.5  14.1   2  0.5  2  3  2
202211300900 162   2  4.9   2 11.0  703 1023.2 1027.1  2   3.5   2.9  -6.5  50.0   3.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        7   5   74 -         -9  -9  -9  2000  0.1 -9.00 -9  11.0 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 165   2  7.6  27 24.0  607 1025.0 1030.7  2   3.0  -0.5  -3.0  83.0   4.9    0.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 85 88 08                       8   8    4 CuSc       0   0   8  2263  0.0  0.08 -9   1.4   8.0   9.5  11.1  12.0   3  1.0  4  1  1
202211300900 168  32  9.2  32 28.0  536 1019.6 1028.0  2   3.7   0.8 -10.3  43.0   2.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   0   -9 Ci         2   0   0  2000  0.0  0.36 -9   1.2   8.0   9.8  12.5  13.6   3  1.0  5  3  2
202211300900 169  36 16.3  36 23.0  614 1020.7 1030.2  2   2.7   3.1  -1.8  70.0   5.4   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   9    9 Sc         0   0   5  2483  0.0  0.14 -9   6.1 -99.0 -99.0 -99.0 -99.0   6  4.5  7  3  2
202211300900 170  34  6.0  34 13.0  634 1025.5 1030.0  2   3.7   2.1  -3.6  66.0   4.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10  10   10 -         -9  -9  -9  2000  0.1 -9.00 -9   1.8 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 172   2  8.8  34 17.0  311 1024.9 1031.7  2   1.8  -2.1  -6.4  72.0   3.8    0.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   0   -9 -         -9  -9  -9  1683  0.0  0.14 -9  -0.2 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  1 -9
202211300900 174  29  5.9  29 15.0  710 1008.4 1029.4  2   2.9  -1.3 -10.1  51.0   2.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        7   0   -9 -         -9  -9  -9  1991  0.3 -9.00 -9   0.1 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 177  36  2.0  -9 -9.0   -9 1030.6 1034.2  2   2.6  -3.8  -6.2  83.0   3.8    0.1    0.1    0.1   -9.0    0.4    0.4    0.4 71 77 05                       9   9    5 Sc         0   0   5   367  0.0  0.16 -9   0.8 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  1  1
202211300900 181  32  4.1  32 13.0  308 1029.0 1033.2  2   2.6  -4.2 -13.5  48.0   2.2   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        2   1   11 -         -9  -9  -9  5000  0.7  0.47 -9  -0.5 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 184   2  6.8   2 17.0  424 1028.3 1030.9  2   2.6   6.3   1.2  70.0   6.7    0.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   9    8 ScAs      -9   2   5  3547  0.0  0.00 -9   7.8  12.9  13.9  15.6  16.0   4  2.5  4  3  2
202211300900 185  36 14.8  34 22.0  536 1018.8 1027.7  2   2.7   6.1   0.6  68.0   6.4    0.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   9    9 -         -9  -9  -9  4322  0.0  0.05 -9   5.8 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  1 -9
202211300900 188  18  3.1   7 16.0  609 1026.5 1029.1  2   2.9   5.3  -0.9  64.0   5.7    0.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10  10    9 -         -9  -9  -9  2892  0.0 -9.00 -9   6.1 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 189   5  1.7  -9 -9.0   -9 1019.6 1026.0  2   3.2   8.8   2.1  63.0   7.1   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   7    9 ScAs      -9   2   5  4584  0.0 -9.00 -9  13.0 -99.0 -99.0 -99.0 -99.0   2  0.5  2  3  2
202211300900 192  36  3.9  36 10.0  625 1024.6 1028.3  2   3.3   1.6 -14.5  29.0   2.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   8   70 -         -9  -9  -9  1346  0.5  0.50 -9   5.4 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 201  29  1.6  36 10.0  321 1028.5 1034.8  2   2.2  -6.2 -16.2  45.0   1.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  5000  1.0 -9.00 -9  -1.3 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 202  34  2.5  -9 -9.0   -9 1028.1 1034.3  2   2.7  -4.6 -17.4  36.0   1.6   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  4064  0.4 -9.00 -9  -1.4 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 203  27  2.4  -9 -9.0   -9 1023.4 1033.9  2   2.5  -4.7 -16.8  38.0   1.6   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  5000  0.9 -9.00 -9  -0.6 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 211  32  0.9  -9 -9.0   -9 1005.6 1031.7  2   2.7  -5.2 -18.3  35.0   1.5   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  5000  0.4 -9.00 -9  -1.7 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 212  29  2.5  -9 -9.0   -9 1015.1 1033.4  2   3.3  -6.0 -18.6  36.0   1.4   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  4507  0.0 -9.00 -9  -4.1 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 216  34  2.6  -9 -9.0   -9  939.3 1028.6  2   4.0  -7.1 -22.5  28.0   1.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        1   0   -9 -         -9  -9  -9  2000  0.3 -9.00 -9  -3.0 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 217  20  2.5   5 13.0  336  991.2 1030.5  2   3.0  -4.2 -17.7  34.0   1.5   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  1880  0.3 -9.00 -9  -0.9   3.2   3.2   5.6   7.2  -9 -9.0 -9  3 -9
202211300900 221  27  3.3  -9 -9.0   -9  997.5 1031.6  2   3.2  -5.6 -16.7  41.0   1.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  4668  0.9 -9.00 -9  -3.5 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 226  32  3.3  25 11.0  415 1010.2 1032.3  2   2.7  -3.7 -15.9  38.0   1.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        4   0   -9 -         -9  -9  -9  4992  0.4 -9.00 -9  -0.3 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 232  29  2.1  36 10.0  556 1022.4 1033.4  2   2.7  -3.7 -13.9  45.0   2.1   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        3   0   -9 -         -9  -9  -9  4861  0.9 -9.00 -9   0.1 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3  2
202211300900 235  36  4.2  -9 -9.0   -9 1030.9 1032.2  2   1.9  -1.7  -9.3  56.0   3.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   9   10 -         -9  -9  -9  3624  0.0 -9.00 -9   3.5 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 236  36  2.7  -9 -9.0   -9 1031.4 1033.1  2   2.5  -2.2  -8.1  64.0   3.3   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   2   10 -         -9  -9  -9  4073  0.4 -9.00 -9   0.1 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 238  34  1.9  -9 -9.0   -9 1010.0 1032.2  2   2.3  -3.5 -11.4  54.0   2.6   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   8    9 -         -9  -9  -9  4996  0.0 -9.00 -9   1.8 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 239  34  3.6  -9 -9.0   -9 1021.6 1033.2  2   2.5  -4.3 -12.7  52.0   2.3   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        5   3    7 -         -9  -9  -9  1414  0.6 -9.00 -9   0.0 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 243   2  3.2  -9 -9.0   -9 1030.9 1032.5  2   2.2  -0.6  -7.6  59.0   3.5   -9.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   8    9 -         -9  -9  -9  5000  0.0 -9.00 -9   2.4 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 244  34  2.4  36 10.0  453 1000.1 1031.6  2   2.6  -2.5 -10.5  54.0   2.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  5000  0.0 -9.00 -9   0.3 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 245   2  3.6   2 11.0  437 1023.4 1032.2  2   2.3  -1.7 -10.2  52.0   2.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   9   11 -         -9  -9  -9  2000  0.2 -9.00 -9  -0.4 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 247   2  3.0  -9 -9.0   -9 1014.7 1031.8  2   2.0  -2.0 -11.5  48.0   2.5   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  5184  0.1 -9.00 -9  -0.1 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 248   2  4.3  34 11.0  412  980.0 1031.6  2   2.0  -4.0 -12.1  53.0   2.4   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  5000  0.0 -9.00 -9  -0.2 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 251  34  4.1  29 10.0  346 1024.2 1031.8  2   1.9  -1.4  -7.9  61.0   3.4   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   7    5 -         -9  -9  -9  4741  0.0  0.18 -9   1.5   5.4  10.1  10.3  11.3  -9 -9.0 -9  3 -9
202211300900 252   5  1.4  36 14.0  457 1027.3 1032.1  2   2.2  -2.3  -4.6  84.0   4.3    0.5    0.6    0.6   -9.0   -9.0   -9.0    1.0 -9 -9 -                       10   2    5 -         -9  -9  -9  3035  0.0  0.00 -9  -0.6   4.8   6.9  10.3  11.1  -9 -9.0 -9  1 -9
202211300900 253  32  4.2  29 13.0  612 1020.3 1027.2  2   3.9   1.4 -16.5  25.0   1.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   0   -9 -         -9  -9  -9  5000  0.5  0.57 -9   4.8   9.5  11.6  13.1  14.1  -9 -9.0 -9  3 -9
202211300900 254  32  4.0  29 12.0  428 1015.5 1032.1  2   2.1  -1.4 -10.2  51.0   2.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   1    4 -         -9  -9  -9  5000  0.2  0.37 -9   0.7   5.1   4.9   7.9   8.8  -9 -9.0 -9  3 -9
202211300900 255  32  5.3  32 14.0  544 1020.8 1027.3  2   3.4   1.4 -13.1  33.0   2.2   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   0   -9 -         -9  -9  -9  5000  0.2  0.47 -9   2.7   8.9   8.4  10.9  12.3  -9 -9.0 -9  3 -9
202211300900 257   2  2.5   2 11.0  653 1026.0 1026.8  2   3.4   3.6 -16.1  22.0   1.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   0   -9 -         -9  -9  -9  2385  0.4  0.53 -9   5.9   7.6   8.5  11.6  13.3  -9 -9.0 -9  3 -9
202211300900 258   2  4.5  34 14.0  644 1030.0 1030.2  2   3.0   0.9  -7.1  55.0   3.6   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        7   1   14 -         -9  -9  -9  5000  0.1  0.31 -9   2.3  10.3  10.4  11.5  12.6  -9 -9.0 -9  3 -9
202211300900 259  32  4.8   7 15.0  429 1027.8 1029.8  2   3.2   0.6  -5.6  63.0   4.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   3    3 -         -9  -9  -9  4830  0.0  0.19 -9   2.4   8.3   9.7  12.3  13.8  -9 -9.0 -9  3 -9
202211300900 260  36  4.3   2 15.0  600 1024.2 1029.8  2   3.2   0.7  -6.6  58.0   3.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   6   11 -         -9  -9  -9  2000  0.1 -9.00 -9   1.6 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 261  36  5.1  34 16.0  410 1028.4 1030.5  2   3.2   0.7  -3.9  71.0   4.6   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   9    7 -         -9  -9  -9  4191  0.0 -9.00 -9   5.0 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 262  34  3.0  36 10.0  733 1022.5 1029.1  2   2.9   0.7  -7.8  53.0   3.4   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   0   -9 -         -9  -9  -9  2000  0.0 -9.00 -9   2.2 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 263  36  4.5  32 10.0  448 1026.4 1028.2  2   3.0   1.7 -12.5  34.0   2.3   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   0   -9 -         -9  -9  -9  5000  0.1  0.45 -9   3.3   6.3  10.3  12.4  13.7  -9 -9.0 -9  3 -9
202211300900 264  27  4.4  27 10.0  542 1011.0 1030.4  2   2.3  -0.8 -15.1  33.0   1.9   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  5000  0.0  0.34 -9   0.1   3.0   3.9   7.8   9.8  -9 -9.0 -9  3 -9
202211300900 266  29  3.4  27 20.0  423 1016.7 1027.9  2   2.3   1.0 -10.2  43.0   2.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   0   -9 -         -9  -9  -9  1781  0.0  0.35 -9   2.4   4.4   6.5  10.4  12.4  -9 -9.0 -9  3 -9
202211300900 268  29  7.9  34 17.0  619 1027.5 1028.7  2   2.0   3.1  -3.9  60.0   4.6   -9.0    0.0    0.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10  -9   -9 -         -9  -9  -9  2000  0.0 -9.00 -9   3.1 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 271  25  2.4  -9 -9.0   -9  986.8 1027.9  2   3.9  -3.1 -15.4  38.0   1.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        4   0   -9 -         -9  -9  -9  2000  0.1 -9.00 -9  -2.6 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 272  29  6.5  32 15.0  344 1002.7 1029.9  2   3.7  -4.3 -15.0  43.0   1.9   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  2000  0.3 -9.00 -9  -2.9 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 273  29  6.0  32 12.0  529 1008.0 1030.3  2   3.1  -4.4 -18.2  33.0   1.5   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        0   0   -9 -         -9  -9  -9  5000  0.3 -9.00 -9  -1.9 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 276  32  4.8  27 11.0  522 1002.2 1028.9  2   3.7  -3.0 -19.8  26.0   1.3   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  5000  0.1  0.37 -9  -1.4   1.4   4.3   7.4   9.1  -9 -9.0 -9  3 -9
202211300900 277  29  5.4  32 13.0  309 1022.6 1027.8  2   4.0  -0.3 -15.4  31.0   1.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        8   0   -9 -         -9  -9  -9  2000  0.0 -9.00 -9   2.3 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 278  29  3.2  -9 -9.0   -9 1019.3 1029.8  2   3.5  -2.0 -17.7  29.0   1.5   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   0   -9 -         -9  -9  -9  5000  0.0 -9.00 -9  -0.6 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 279  29  2.8  34 11.0  750 1024.7 1031.0  2   3.3  -1.5 -16.4  31.0   1.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  5000  0.0 -9.00 -9   0.3 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 281  29  3.7  27 13.0  424 1017.5 1029.8  2   3.2  -1.1 -16.5  30.0   1.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   0   -9 -         -9  -9  -9  5000  0.0 -9.00 -9  -0.1 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 283  32  5.9  34 17.0  651 1023.7 1028.8  2   3.1  -0.7 -17.4  27.0   1.6   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   0   -9 -         -9  -9  -9  1784  0.0  0.28 -9   0.2   4.4   7.5   9.6  12.4  -9 -9.0 -9  3 -9
202211300900 284   2  3.6  -9 -9.0   -9 1000.3 1029.3  2   2.6  -1.6 -12.5  43.0   2.3   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  4884  0.1 -9.00 -9   0.6 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 285  32  2.5  -9 -9.0   -9 1024.8 1028.2  2   2.5   1.3 -16.1  26.0   1.7   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  4949  0.0 -9.00 -9   4.0 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 288  34  5.2  34 13.0  842 1026.7 1027.8  2   2.8   1.1 -18.8  21.0   1.4   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                       10   9   71 -         -9  -9  -9  5000  0.2 -9.00 -9   1.9 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 289  29  5.8  27 17.0  647 1012.5 1030.1  2   2.6  -0.7 -12.6  40.0   2.3   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        9   0   -9 -         -9  -9  -9  4814  0.0 -9.00 -9   0.9 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 294  34  1.7  34 10.0  427 1021.7 1027.4  2   3.7   2.9  -8.1  44.0   3.3   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        7   0   -9 -         -9  -9  -9  5000  0.1 -9.00 -9   5.3 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
202211300900 295  36  0.9  -9 -9.0   -9 1021.8 1027.6  2   3.3   3.2  -6.5  49.0   3.8   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0   -9.0 -9 -9 -                        7   0   -9 -         -9  -9  -9  2000  0.1 -9.00 -9   5.9 -99.0 -99.0 -99.0 -99.0  -9 -9.0 -9  3 -9
#7777END
"""
    myTable = Table(data)
    print(*myTable.data, sep='\n')
    print(myTable.header)