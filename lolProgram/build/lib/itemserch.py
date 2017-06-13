# RGAPI-bb875549-7272-48f0-b9e4-2828cdbb6356

import json
import urllib.request
import re
def text(str):
    s = str
    hangul = re.compile('[^ ㄱ-ㅣ가-힣|0-9|%|+|.]+') # 한글과 띄어쓰기를 제외한 모든 글자
    result = hangul.sub('', s) # 한글과 띄어쓰기를 제외한 모든 부분을 제거
    return (result)

def itemsearch(item_input):
    KEY = "RGAPI-bb875549-7272-48f0-b9e4-2828cdbb6356"
    Data = []

    REGION_ENDPOINT_ITEM = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/ko_KR/item.json"
    response_item = urllib.request.urlopen((REGION_ENDPOINT_ITEM + "?&api_key={0}").format(KEY))
    rescode_item = response_item.getcode()
    response_body_item = response_item.read()

    item_data = json.loads(response_body_item.decode('utf-8'))
    find_success = False

    f = open('recent_data.txt', 'r')
    recently_ID = json.load(f)
    f.close()

    recently_ID.insert(0, item_input)

    if (recently_ID.__len__() > 5):
        recently_ID.pop()

    f = open('recent_data.txt', 'w')
    json.dump(recently_ID, f)
    f.close()

    for i in item_data['data']:
        if item_data['data'][i]['name'] == item_input:
            itemid = i
            Data.append('\n\n\n\n\n\n\n')
            Data.append('아이템 설명: ')
            Data.append(text(item_data['data'][i]['description']))
            Data.append('\n\n')
            Data.append('아이템 요약')
            Data.append(text(item_data['data'][i]['plaintext']))
            if item_data['data'][i]['colloq'] != ' ':
                Data.append('\n\n')
                Data.append('별명: ')
                Data.append(text(item_data['data'][i]['colloq']))
            Data.append('\n\n')
            Data.append("아이템 가격: ")
            Data.append(item_data['data'][i]['gold']['total'])
            Data.append('\n\n')
            find_success = True
    if find_success == False:
        Data.append('찾지 못한 아이템')
    print(type(itemid))
    return Data, itemid


