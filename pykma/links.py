from .utils.kmaurl import URLManager

# ASOS 
ASOS_SPECIFIC_TIME_REQUEST = URLManager("https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php")
ASOS_TERM_REQUEST          = URLManager("https://apihub.kma.go.kr/api/typ01/url/kma_sfctm3.php")
ASOS_DAILY_REQUEST         = URLManager("https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd.php")
ASOS_DAILY_TERM_REQUEST    = URLManager("https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd3.php")
ASOS_ELEMENT_REQUEST       = URLManager("https://apihub.kma.go.kr/api/typ01/url/kma_sfctm5.php")

GROUND_AVERAGE_REQUEST     = URLManager("https://apihub.kma.go.kr/api/typ01/url/sfc_norm1.php")

# YEAR_SUMMARY_REQUEST       = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getYearSumry")
# YEAR_SUMMARY_2_REQUEST     = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getYearSumry2")

# AVERAGE_ANNUAL_TEMP_DIFF   = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getAvgTaAnamaly")
# AVERAGE_ANNUAL_RAIN_DIFF   = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getAvgRnAnamaly")
# STATION_CURRENT_DATA       = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getStnPhnmnData")
# STATION_CURRENT_DATA_2     = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getStnPhnmnData2")
# STATION_CURRENT_DATA_3     = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getStnPhnmnData3")

# GET_NOTE_REQUEST           = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getNote")
# STATION_NOTE_REQUEST       = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getSfcStnLstTbl")
# MONTHLY_SUMMARY_REQUEST    = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getMmSumry")
# MONTHLY_SUMMARY_REQUEST_2  = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getMmSumry2")
# DAILY_WEATHER_BY_MONTH     = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/SfcMtlyInfoService/getDailyWthrData")

# GRAPIC_GROUND_WEATHER      = URLManager("https://apihub.kma.go.kr/api/typ03/php/alw/sfc/sfc_ww_pnt.php")

# AWS

AWS_MINUTES_REQUEST        = URLManager("https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min")
AWS_TEMP_REQUEST           = URLManager("https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_lst")

AWS_CLOUD_REQUEST          = URLManager("https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_cloud")
AWS_AVERAGE_CLOUD_REQUEST  = URLManager("https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ca2")
AWS_HEIGHT_CLOUD_REQUEST   = URLManager("https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ca3")

AWS_VISIBILITY_REQUEST     = URLManager("https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_vis")
AWS_AVERAGE_VISI_REQUEST   = URLManager("https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_vis3")

AWS_CURRENT_WEATHER        = URLManager("https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ww1")
AWS_ANALYSIS_CUR_WEATHER   = URLManager("https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min_ww2")

MOBILE_AWS_REQUEST         = URLManager("https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws3_min_mob")
AWS_HOURLY_REQUEST         = URLManager("https://apihub.kma.go.kr/api/typ01/url/awsh.php")
AWS_ELEMENT_REQUEST        = URLManager("https://apihub.kma.go.kr/api/typ01/url/sfc_aws_day.php")

# AWS_STATION_MONTLY_SUMMARY = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/AwsYearlyInfoService/getStnbyMmSumry")
# AWS_YEAR_SUMMARY           = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/AwsYearlyInfoService/getYearSumry")
# AWS_STATION_REQUEST        = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/AwsYearlyInfoService/getAwsStnLstTbl")
# AWS_YEARLY_NOTE            = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/AwsYearlyInfoService/getNote")

# AWS_DAILY_REQUEST          = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/AwsMtlyInfoService/getDailyAwsData")
# AWS_MONTHLY_SUMMARY        = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/AwsMtlyInfoService/getMmSumry")
# AWS_STATION_NOTE           = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/AwsMtlyInfoService/getAwsStnLstTbl")
# AWS_MONTHLY_NOTE           = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/AwsMtlyInfoService/getNote")

# AWS_GRAPHIC_CUR_WEATHER    = URLManager("https://apihub.kma.go.kr/api/typ03/php/alw/aws/aws_ww_pnt.php")
# AWS_GRAPHIC_DAY_STATIC     = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_day_img1")
# AWS_GRAPHIC_DISTRIBUTION   = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_min_img1")
# AWS_GRAPHIC_DISTRIBUTION_2 = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_min_img2")
# AWS_GRAPHIC_DOT_DISTRIBUTE = URLManager("https://apihub.kma.go.kr/api/typ03/php/alw/aws/aws_obs_pnt.php")
# AWS_GRAPHIC_SEE_DISTRIBUTE = URLManager("https://apihub.kma.go.kr/api/typ03/php/alw/sea/sea_obs_pnt.php")

# AWS_GRAPHIC_6HOUR_SERIES   = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-awsm_tms_h06")
# AWS_GRAPHIC_12HOUR_SERIES  = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-awsm_tms_h12")
# AWS_GRAPHIC_24HOUR_SERIES  = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws2/nph-awsm_tms_h24")
# AWS_GRAPHIC_2DAYS_SERIES   = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws2/nph-awsm_tms_d02")
# AWS_GRAPHIC_4DAYS_SERIES   = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws2/nph-awsm_tms_d04")
# AWS_GRAPHIC_8DAYS_SERIES   = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws2/nph-awsm_tms_d08")
# AWS_GRAPHIC_12DAYS_SERIES  = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws2/nph-awsm_tms_d12")

# AWS_GRAPHIC_DAILY_MAX_TEMP_NO_BACKGROUND = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_day_imgp1")
# AWS_GRAPHIC_RAIN_DETECTION_NO_BACKGROUND = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_min_imgp1")
# AWS_GRAPHIC_WIND_VECTOR_NO_BACKGROUND    = URLManager("https://apihub.kma.go.kr/api/typ03/cgi/aws3/nph-aws_min_imgp2")

# North Korea
NORTH_KOREA_GROUND         = URLManager("https://apihub.kma.go.kr/api/typ01/url/nko_sfctm.php")
NORTH_KOREA_ANNUAL         = URLManager("https://apihub.kma.go.kr/api/typ01/url/sfc_nko_norm1.php")

# Yellow Dust
PM10_DATA_REQUEST          = URLManager("https://apihub.kma.go.kr/api/typ01/url/kma_pm10.php")
YELLOW_DUST_LOCATION       = URLManager("https://apihub.kma.go.kr/api/typ01/url/stn_pm10_inf.php")
YELLOW_DUST_DATA           = URLManager("https://apihub.kma.go.kr/api/typ01/url/dst_pm10_tm.php")
YELLOW_DUST_HOUR_STATISTIC = URLManager("https://apihub.kma.go.kr/api/typ01/url/dst_pm10_hr.php")
# YD_GRAPHIC_SATELLITE       = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/YdstInfoService/getYdstSatlitImg")
# YD_GRAPHIC_REQUEST         = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/YdstInfoService/getYdstObs")
# YD_GRAPHIC_WEATHER_CHART   = URLManager("https://apihub.kma.go.kr/api/typ02/openApi/YdstInfoService/getYdstSfcChart")

# Snow
SNOW_LOCATION              = URLManager("https://apihub.kma.go.kr/api/typ01/url/stn_snow.php")
SNOW_DATA                  = URLManager("https://apihub.kma.go.kr/api/typ01/url/kma_snow1.php")
SNOW_TERM                  = URLManager("https://apihub.kma.go.kr/api/typ01/url/kma_snow2.php")
SNOW_DAILY                 = URLManager("https://apihub.kma.go.kr/api/typ01/url/kma_snow_day.php")

# Ultraviolet
UV_DATA                    = URLManager("https://apihub.kma.go.kr/api/typ01/url/kma_sfctm_uv.php")

# AWS 객관 분석
# 계절관측

# Station Information
STATION_INFO               = URLManager("https://apihub.kma.go.kr/api/typ01/url/stn_inf.php")