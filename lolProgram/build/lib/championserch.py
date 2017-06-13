from PIL import Image, ImageTk
import urllib
import urllib.request

def championserch(champion):
    import urllib.request
    import json
    KEY = "RGAPI-bb875549-7272-48f0-b9e4-2828cdbb6356"
    data = []
    REGION_ENDPOINT_CHAMPION = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/ko_KR/champion.json"
    response_champion = urllib.request.urlopen((REGION_ENDPOINT_CHAMPION + "?&api_key={0}").format(KEY))
    rescode_champion = response_champion.getcode()
    response_body_champion = response_champion.read()
    champion_data = json.loads(response_body_champion.decode('utf-8'))
    find_success = False

    f = open('recent_data.txt', 'r')
    recently_ID = json.load(f)
    f.close()

    recently_ID.insert(0, champion)

    if (recently_ID.__len__() > 5):
        recently_ID.pop()

    f = open('recent_data.txt', 'w')
    json.dump(recently_ID, f)
    f.close()

    for i in champion_data['data']:
        if champion_data['data'][i]['name'] == champion:
            championname = i
            data.append('☆ 챔피언 이름: ')
            data.append(champion_data['data'][i]['name'])
            data.append('\n\n')
            data.append('☆ 챔피언 이미지: ')
          #  img = Image.open(champion_data['data'][i]['image']['full'])
          #  data.append(img.show())
            data.append(champion_data['data'][i]['title'])
            data.append('\n\n')
            data.append('☆ 챔피언 배경: ')
            data.append(champion_data['data'][i]['blurb'])
            data.append('\n\n')
            data.append('☆ 챔피언 능력치 ')
            data.append('\n\n')
            data.append('\t- 공격력: ')
            data.append(champion_data['data'][i]['info']['attack'])
            data.append('\n\n')
            data.append('\t- 주문력: ')
            data.append(champion_data['data'][i]['info']['magic'])
            data.append('\n\n')
            data.append('\t- 난이도: ')
            data.append(champion_data['data'][i]['info']['difficulty'])
            data.append('\n\n')
            data.append('\t- 방어력: ')
            data.append(champion_data['data'][i]['info']['defense'])
            data.append('\n\n')
            find_success = True
    if find_success == False:
        data.append('찾지 못한 챔피언')

    return data, championname


