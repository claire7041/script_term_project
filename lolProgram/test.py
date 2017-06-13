def favoritesinsert(data, type):
    import json
    import urllib.request
    from collections import OrderedDict

    KEY = "RGAPI-bb875549-7272-48f0-b9e4-2828cdbb6356"

    REGION_ENDPOINT_CHAMPION = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/ko_KR/champion.json"
    response_champion = urllib.request.urlopen((REGION_ENDPOINT_CHAMPION + "?&api_key={0}").format(KEY))
    rescode_champion = response_champion.getcode()
    response_body_champion = response_champion.read()
    champion_data = json.loads(response_body_champion.decode('utf-8'))
    find_success = False

    REGION_ENDPOINT_ITEM = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/ko_KR/item.json"
    response_item = urllib.request.urlopen((REGION_ENDPOINT_ITEM + "?&api_key={0}").format(KEY))
    rescode_item = response_item.getcode()
    response_body_item = response_item.read()

    item_data = json.loads(response_body_item.decode('utf-8'))

    favorites_data = OrderedDict()
    favorites_data['champion'] = ['없음']
    favorites_data['item'] = ['없음']
    favorites_data['player'] = ['없음']

    f = open('favorites.txt', 'r')
    loadfavorites = json.load(f)
    f.close()
    if len(loadfavorites['champion']) == 0:
        pass
    else:
        favorites_data['champion'] = loadfavorites['champion']

    if len(loadfavorites['item']) == 0:
        pass
    else:
        favorites_data['item'] = loadfavorites['item']
    if len(loadfavorites['player']) == 0:
        pass
    else:
        favorites_data['player'] = loadfavorites['player']
    existence = True
    print(favorites_data['champion'])
    if type == 1:
        for k in champion_data['data']:
            if champion_data['data'][k]['name'] == data:
                if data in favorites_data['champion']:
                    favorites_data['champion'].remove(data)
                    if len(favorites_data['champion']) == 0:
                        favorites_data['champion'].append('없음')
                    break
                else:
                    if favorites_data['champion'][0] == '없음':
                        favorites_data['champion'].remove('없음')
                    favorites_data['champion'].append(data)
                break
            else:
                existence = False
    elif type == 2:
        for k in item_data['data']:
            if item_data['data'][k]['name'] == data:
                for i in favorites_data['item']:
                    if i == data:
                        favorites_data['item'].remove(data)
                        if len(favorites_data['item']) == 0:
                            favorites_data['item'].append('없음')
                    else:
                        if i == '없음':
                            favorites_data['item'].remove('없음')
                        favorites_data['item'].append(data)
                        existence = True
                        break
            else:
                existence = False
    elif type == 3:
        for i in favorites_data['player']:
            if i == data:
                favorites_data['player'].remove(data)
                if len(favorites_data['player']) == 0:
                    favorites_data['player'].append('없음')
                existence = True
                break
            else:
                if i == '없음':
                    favorites_data['player'].remove('없음')
                else:
                    favorites_data['player'].append(data)
                existence=True
    else:
        print('잘못입력하셨습니다.')
    if existence == False:
        print('찾을 수 없는 데이터를 입력하셨습니다.')

    print(favorites_data['champion'])
    f = open('favorites.txt', 'w')
    json.dump(favorites_data, f)
    f.close()
    return favorites_data

def favoritesDelete(removedata):
    import json
    f = open('favorites.txt', 'r')
    favorites2 = json.load(f)
    f.close()

    print('즐겨찾기 목록')
    print('champion')
    print(favorites2['champion'])
    print('item')
    print(favorites2['item'])
    print('player')
    print(favorites2['player'])

    removetype = input('즐겨찾기를 제거할 분야를 선택 [1. 챔피언 2.아이템 3.소환사]: ')
    if removetype == '1':
        if favorites2['champion'][0] != '없음':
            print('챔피언 즐겨찾기 목록')
            for i in range(0, len(favorites2['champion'])):
                print(favorites2['champion'][i])
            for i in favorites2['champion']:
                if i == removedata:
                    favorites2['champion'].remove(removedata)
                    if len(favorites2['champion']) == 0:
                        favorites2['champion'].append('없음')
                    break
                else:
                    pass
        else:
            print('제거할 수 없습니다.')

    elif removetype == '2':
        if favorites2['item'][0] != '없음':
            print('아이템 즐겨찾기 목록')
            for i in range(0, len(favorites2['item'])):
                print(favorites2['item'][i])
            removedata = input('제거할 아이템의 이름을 입력하세요: ')
            for i in favorites2['item']:
                if i == removedata:
                    favorites2['item'].remove(removedata)
                    if len(favorites2['item']) == 0:
                        favorites2['item'].append('없음')
                    break
                else:
                    pass
        else:
            print('제거할 수 없습니다.')
    elif removetype == '3':
        if favorites2['player'][0] != '없음':
            print('소환사 즐겨찾기 목록')
            for i in range(0, len(favorites2['player'])):
                print(favorites2['player'][i])
            removedata = input('제거할 소환사의 이름을 입력하세요: ')
            for i in favorites2['player']:
                if i == removedata:
                    favorites2['player'].remove(removedata)
                    if len(favorites2['player']) == 0:
                        favorites2['player'].append('없음')
                    break
                else:
                    pass
        else:
            print('제거할 수 없습니다.')

    print(favorites2)
    f = open('favorites.txt', 'w')
    json.dump(favorites2, f)
    f.close()
    return favorites2

favoritesinsert('아리', 1)