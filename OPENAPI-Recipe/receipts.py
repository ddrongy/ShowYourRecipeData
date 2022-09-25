# 라이브러리 import
import requests
import pprint
import json
from pandas import Series, DataFrame
import pandas as pd
# url 입력

def crawling(key, startnum, endnum):
    url = 'http://openapi.foodsafetykorea.go.kr/api/'+key+'/COOKRCP01/json/'+str(startnum)+'/' + str(endnum)

    response = requests.get(url)

    contents = response.text
    json_ob = json.loads(contents)
    body = json_ob['COOKRCP01']['row']

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

    return df

def main():
    # 크롤링 한번에 1000개 call가능
    # data num = 1부터 시작
    key = "d5930f67722c49129a56"
    df1 = crawling(key, 1, 1000)
    df2 = crawling(key, 1001, 2000)
    result = pd.concat([df1, df2])
    result.to_csv('openapi-recipe.csv', index=False)

if __name__ == "__main__":
    main()