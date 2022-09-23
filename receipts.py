# 라이브러리 import
import requests
import pprint
import json
from pandas import Series, DataFrame
import pandas as pd
# url 입력
url = 'http://openapi.foodsafetykorea.go.kr/api/d5930f67722c49129a56/COOKRCP01/json/1/1000'

# url 불러오기
response = requests.get(url)

#데이터 값 출력해보기
contents = response.text
# json_ob = json.loads(contents)
#         response = requests.get(url)
#         contents = response.text
json_ob = json.loads(contents)
body = json_ob['COOKRCP01']['row']

# body = json_ob['COOKRCP01']['row']
# print(body)

메뉴명 = [ e["RCP_NM"] for e in body ]
요리종류 = [ e["RCP_PAT2"] for e in body ]
중량 = [ e["INFO_WGT"] for e in body ]
열량 = [ e["INFO_ENG"] for e in body ]
탄수화물 = [ e["INFO_CAR"] for e in body ]
단백질 = [ e["INFO_PRO"] for e in body ]
지방 = [ e["INFO_FAT"] for e in body ]
나트륨 = [ e["INFO_NA"] for e in body ]
해쉬태그 = [ e["HASH_TAG"] for e in body ]
재료정보 = [ e["RCP_PARTS_DTLS"] for e in body ]
#ATT_FILE_NO_MK
# print(receipt_name)
# print(receipt_img)

df = DataFrame( columns=['메뉴명', '요리종류', '중량', '열량', '탄수화물', '단백질', '지방', '나트륨', '해쉬태그', '재료정보'])
df['메뉴명'] = 메뉴명
df['요리종류'] =요리종류
df['중량'] = 중량
df['열량'] = 열량
df['탄수화물'] = 탄수화물
df['단백질'] = 단백질
df['지방'] = 지방
df['나트륨'] = 나트륨
df['해쉬태그'] = 해쉬태그
df['재료정보'] = 재료정보

df.to_csv('dd.csv')

url = 'http://openapi.foodsafetykorea.go.kr/api/d5930f67722c49129a56/COOKRCP01/json/1001/2000'

# url 불러오기
response = requests.get(url)

#데이터 값 출력해보기
contents = response.text
# json_ob = json.loads(contents)
#         response = requests.get(url)
#         contents = response.text
json_ob = json.loads(contents)
body = json_ob['COOKRCP01']['row']

# body = json_ob['COOKRCP01']['row']
# print(body)

메뉴명 = [ e["RCP_NM"] for e in body ]
요리종류 = [ e["RCP_PAT2"] for e in body ]
중량 = [ e["INFO_WGT"] for e in body ]
열량 = [ e["INFO_ENG"] for e in body ]
탄수화물 = [ e["INFO_CAR"] for e in body ]
단백질 = [ e["INFO_PRO"] for e in body ]
지방 = [ e["INFO_FAT"] for e in body ]
나트륨 = [ e["INFO_NA"] for e in body ]
해쉬태그 = [ e["HASH_TAG"] for e in body ]
재료정보 = [ e["RCP_PARTS_DTLS"] for e in body ]
#ATT_FILE_NO_MK
# print(receipt_name)
# print(receipt_img)

df1 = DataFrame( columns=['메뉴명', '요리종류', '중량', '열량', '탄수화물', '단백질', '지방', '나트륨', '해쉬태그', '재료정보'])
df1['메뉴명'] = 메뉴명 
df1['요리종류'] =요리종류
df1['중량'] = 중량
df1['열량'] = 열량
df1['탄수화물'] = 탄수화물
df1['단백질'] = 단백질
df1['지방'] = 지방
df1['나트륨'] = 나트륨
df1['해쉬태그'] = 해쉬태그
df1['재료정보'] = 재료정보

df1.to_csv('dd1.csv')

df = pd.concat([df1, df])
df.reset_index(drop=True)

df.to_csv('food-recipe.csv')