from bs4 import BeautifulSoup

xml_data = """
<mealServiceDietInfo>
<head>
<list_total_count>3</list_total_count>
<RESULT>
<CODE>INFO-000</CODE>
<MESSAGE>정상 처리되었습니다.</MESSAGE>
</RESULT>
</head>
<row>
<ATPT_OFCDC_SC_CODE>
<![CDATA[ G10 ]]>
</ATPT_OFCDC_SC_CODE>
<ATPT_OFCDC_SC_NM>
<![CDATA[ 대전광역시교육청 ]]>
</ATPT_OFCDC_SC_NM>
<SD_SCHUL_CODE>
<![CDATA[ 7430048 ]]>
</SD_SCHUL_CODE>
<SCHUL_NM>
<![CDATA[ 대전대신고등학교 ]]>
</SCHUL_NM>
<MMEAL_SC_CODE>
<![CDATA[ 1 ]]>
</MMEAL_SC_CODE>
<MMEAL_SC_NM>
<![CDATA[ 조식 ]]>
</MMEAL_SC_NM>
<MLSV_YMD>
<![CDATA[ 20231212 ]]>
</MLSV_YMD>
<MLSV_FGR>
<![CDATA[ 158.00 ]]>
</MLSV_FGR>
<DDISH_NM>
<![CDATA[ 김치콩나물국 (5.6.9)<br/>닭고구마조림 (5.6.13.15)<br/>총각김치 (9)<br/>초코시리얼/우유 (2.5.6)<br/>식빵/딸기쨈 (2.5.6.13)<br/>찰흑미밥 ]]>
</DDISH_NM>
<ORPLC_INFO>
<![CDATA[ 쇠고기(종류) : 국내산(한우)<br/>쇠고기 식육가공품 : 국내산<br/>돼지고기 : 국내산<br/>돼지고기 식육가공품 : 국내산<br/>닭고기 : 국내산<br/>닭고기 식육가공품 : 국내산<br/>오리고기 : 국내산<br/>오리고기 가공품 : 국내산<br/>쌀 : 국내산<br/>배추 : 국내산<br/>고춧가루 : 국내산<br/>콩 : 국내산<br/>낙지 : 국내산<br/>고등어 : 국내산<br/>갈치 : 국내산<br/>오징어 : 국내산<br/>꽃게 : 국내산<br/>참조기 : 국내산<br/>비고 : ]]>
</ORPLC_INFO>
<CAL_INFO>
<![CDATA[ 950.8 Kcal ]]>
</CAL_INFO>
<NTR_INFO>
<![CDATA[ 탄수화물(g) : 155.9<br/>단백질(g) : 39.8<br/>지방(g) : 16.3<br/>비타민A(R.E) : 250.1<br/>티아민(mg) : 0.7<br/>리보플라빈(mg) : 1.0<br/>비타민C(mg) : 29.0<br/>칼슘(mg) : 1110.4<br/>철분(mg) : 4.6 ]]>
</NTR_INFO>
<MLSV_FROM_YMD>
<![CDATA[ 20231212 ]]>
</MLSV_FROM_YMD>
<MLSV_TO_YMD>
<![CDATA[ 20231212 ]]>
</MLSV_TO_YMD>
<LOAD_DTM>
<![CDATA[ 20231211 ]]>
</LOAD_DTM>
</row>
<row>
<ATPT_OFCDC_SC_CODE>
<![CDATA[ G10 ]]>
</ATPT_OFCDC_SC_CODE>
<ATPT_OFCDC_SC_NM>
<![CDATA[ 대전광역시교육청 ]]>
</ATPT_OFCDC_SC_NM>
<SD_SCHUL_CODE>
<![CDATA[ 7430048 ]]>
</SD_SCHUL_CODE>
<SCHUL_NM>
<![CDATA[ 대전대신고등학교 ]]>
</SCHUL_NM>
<MMEAL_SC_CODE>
<![CDATA[ 2 ]]>
</MMEAL_SC_CODE>
<MMEAL_SC_NM>
<![CDATA[ 중식 ]]>
</MMEAL_SC_NM>
<MLSV_YMD>
<![CDATA[ 20231212 ]]>
</MLSV_YMD>
<MLSV_FGR>
<![CDATA[ 1465.00 ]]>
</MLSV_FGR>
<DDISH_NM>
<![CDATA[ 배추김치 (9)<br/>수수밥 <br/>꼬치없는소떡소떡 (2.5.6.10.12.13.15.16)<br/>김자반 (5)<br/>굴림만두국 (1.5.6.10.16.18) ]]>
</DDISH_NM>
<ORPLC_INFO>
<![CDATA[ 쇠고기(종류) : 국내산(한우)<br/>쇠고기 식육가공품 : 국내산<br/>돼지고기 : 국내산<br/>돼지고기 식육가공품 : 국내산<br/>닭고기 : 국내산<br/>닭고기 식육가공품 : 국내산<br/>오리고기 : 국내산<br/>오리고기 가공품 : 국내산<br/>쌀 : 국내산<br/>배추 : 국내산<br/>고춧가루 : 국내산<br/>콩 : 국내산<br/>낙지 : 국내산<br/>고등어 : 국내산<br/>갈치 : 국내산<br/>오징어 : 국내산<br/>꽃게 : 국내산<br/>참조기 : 국내산<br/>비고 : ]]>
</ORPLC_INFO>
<CAL_INFO>
<![CDATA[ 882.7 Kcal ]]>
</CAL_INFO>
<NTR_INFO>
<![CDATA[ 탄수화물(g) : 116.3<br/>단백질(g) : 30.9<br/>지방(g) : 32.4<br/>비타민A(R.E) : 71.0<br/>티아민(mg) : 0.7<br/>리보플라빈(mg) : 0.4<br/>비타민C(mg) : 27.4<br/>칼슘(mg) : 848.6<br/>철분(mg) : 6.5 ]]>
</NTR_INFO>
<MLSV_FROM_YMD>
<![CDATA[ 20231212 ]]>
</MLSV_FROM_YMD>
<MLSV_TO_YMD>
<![CDATA[ 20231212 ]]>
</MLSV_TO_YMD>
<LOAD_DTM>
<![CDATA[ 20231211 ]]>
</LOAD_DTM>
</row>
<row>
<ATPT_OFCDC_SC_CODE>
<![CDATA[ G10 ]]>
</ATPT_OFCDC_SC_CODE>
<ATPT_OFCDC_SC_NM>
<![CDATA[ 대전광역시교육청 ]]>
</ATPT_OFCDC_SC_NM>
<SD_SCHUL_CODE>
<![CDATA[ 7430048 ]]>
</SD_SCHUL_CODE>
<SCHUL_NM>
<![CDATA[ 대전대신고등학교 ]]>
</SCHUL_NM>
<MMEAL_SC_CODE>
<![CDATA[ 3 ]]>
</MMEAL_SC_CODE>
<MMEAL_SC_NM>
<![CDATA[ 석식 ]]>
</MMEAL_SC_NM>
<MLSV_YMD>
<![CDATA[ 20231212 ]]>
</MLSV_YMD>
<MLSV_FGR>
<![CDATA[ 423.00 ]]>
</MLSV_FGR>
<DDISH_NM>
<![CDATA[ 알감자미트볼조림 (1.2.5.6.10.12.13.15.16)<br/>오징어덮밥&달걀후라이 (5.6.13.17)<br/>배추김치 (9)<br/>귤 <br/>미소된장국 (5.6) ]]>
</DDISH_NM>
<ORPLC_INFO>
<![CDATA[ 쇠고기(종류) : 국내산(한우)<br/>쇠고기 식육가공품 : 국내산<br/>돼지고기 : 국내산<br/>돼지고기 식육가공품 : 국내산<br/>닭고기 : 국내산<br/>닭고기 식육가공품 : 국내산<br/>오리고기 : 국내산<br/>오리고기 가공품 : 국내산<br/>쌀 : 국내산<br/>배추 : 국내산<br/>고춧가루 : 국내산<br/>콩 : 국내산<br/>낙지 : 국내산<br/>고등어 : 국내산<br/>갈치 : 국내산<br/>오징어 : 국내산<br/>꽃게 : 국내산<br/>참조기 : 국내산<br/>비고 : ]]>
</ORPLC_INFO>
<CAL_INFO>
<![CDATA[ 902.5 Kcal ]]>
</CAL_INFO>
<NTR_INFO>
<![CDATA[ 탄수화물(g) : 140.7<br/>단백질(g) : 41.8<br/>지방(g) : 18.5<br/>비타민A(R.E) : 194.7<br/>티아민(mg) : 0.7<br/>리보플라빈(mg) : 0.7<br/>비타민C(mg) : 49.1<br/>칼슘(mg) : 1608.9<br/>철분(mg) : 4.2 ]]>
</NTR_INFO>
<MLSV_FROM_YMD>
<![CDATA[ 20231212 ]]>
</MLSV_FROM_YMD>
<MLSV_TO_YMD>
<![CDATA[ 20231212 ]]>
</MLSV_TO_YMD>
<LOAD_DTM>
<![CDATA[ 20231211 ]]>
</LOAD_DTM>
</row>
</mealServiceDietInfo>
"""

soup = BeautifulSoup(xml_data, 'xml')

# Find all <DDISH_NM> tags
ddish_tags = soup.find_all('DDISH_NM')

# Extract and print the content inside <DDISH_NM> tags
for ddish_tag in ddish_tags:
    content = ddish_tag.get_text(strip=True)
    print(content)
