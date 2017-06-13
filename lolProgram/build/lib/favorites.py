def favoritesinsert(data, type):
    import json
    import urllib.request
    from collections import OrderedDict

    KEY = "RGAPI-bb875549-7272-48f0-b9e4-2828cdbb6356"

    REGION_ENDPOINT_CHAMPION = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/ko_KR/champion.json"
    response_champion = urllib.request.urlopen((REGION_ENDPOINT_CHAMPION + "?&api_key={0}").format(KEY))
    response_body_champion = response_champion.read()
    champion_data = json.loads(response_body_champion.decode('utf-8'))

    REGION_ENDPOINT_ITEM = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/ko_KR/item.json"
    response_item = urllib.request.urlopen((REGION_ENDPOINT_ITEM + "?&api_key={0}").format(KEY))
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
                if data in favorites_data['item']:
                    favorites_data['item'].remove(data)
                    if len(favorites_data['item']) == 0:
                        favorites_data['item'].append('없음')
                    break
                else:
                    if favorites_data['item'][0] == '없음':
                        favorites_data['item'].remove('없음')
                    favorites_data['item'].append(data)
                break
            else:
                existence = False
    elif type == 3:
        if data in favorites_data['player']:
            favorites_data['player'].remove(data)
            if len(favorites_data['player']) == 0:
                favorites_data['player'].append('없음')
        else:
            if favorites_data['player'][0] == '없음':
                favorites_data['player'].remove('없음')
            favorites_data['player'].append(data)
    else:
        print('잘못입력하셨습니다.')
    if existence == False:
        print('찾을 수 없는 데이터를 입력하셨습니다.')

    print(favorites_data)
    f = open('favorites.txt', 'w')
    json.dump(favorites_data, f)
    f.close()
    return favorites_data



