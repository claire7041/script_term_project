#import os
#import sys

import urllib.request
import ast
import json
from time import localtime, strftime

"""
https://kr.api.pvp.net/api/lol/kr/.../?api_key=RGAPI-bb875549-7272-48f0-b9e4-2828cdbb6356
"""

REGION_ENDPOINT = "https://kr.api.riotgames.com"
KEY = "RGAPI-bb875549-7272-48f0-b9e4-2828cdbb6356"

def searchsummoner(ID):
    #ID = input("소환사의 이름을 입력하세요: ")
    f = open('recent_data.txt', 'r')
    recently_ID = json.load(f)
    f.close()

    recently_ID.insert(0, ID)

    if (recently_ID.__len__() > 5):
        recently_ID.pop()

    f = open('recent_data.txt', 'w')
    json.dump(recently_ID, f)
    f.close()
    Data = []
    if(len(ID) == 1):
        Data.append("잘못 입력하셨습니다. 다시 입력해주세요")
    else:
        # 띄어쓰기 삭제
        ID = ID.split()
        my_ID = ""
        my_ID = my_ID.join(ID)

        # 소환사 검색
        response_summoner = urllib.request.urlopen((REGION_ENDPOINT + "/lol/summoner/v3/summoners/by-name/{0}?&api_key={1}").format(my_ID, KEY))
        rescode_summoner = response_summoner.getcode()

        if(rescode_summoner == 200):
            response_body_summoner = response_summoner.read()
            # 딕셔너리로 변경
            summoner_dict = ast.literal_eval(response_body_summoner.decode('utf-8'))

        # id 값 ID_NUM으로 옮김
        ID_NUM = summoner_dict['id']
        ID_ACCOUNT = summoner_dict['accountId']

        # 리그 검색
        response_league = urllib.request.urlopen((REGION_ENDPOINT + "/lol/league/v3/positions/by-summoner/{0}?&api_key={1}").format(ID_NUM, KEY))
        rescode_league = response_league.getcode()

        if (rescode_league == 200):
            response_body_league = response_league.read()

        league_str = response_body_league.decode('utf-8')
        league_str = league_str.replace('[', '')
        league_str = league_str.replace(']', '')
        league_dict = json.loads(league_str)

        # 최근 전적 검색
        response_recent = urllib.request.urlopen((REGION_ENDPOINT + "/lol/match/v3/matchlists/by-account/{0}/recent?&api_key={1}").format(ID_ACCOUNT, KEY))
        rescode_recent = response_recent.getcode()

        if (rescode_recent == 200):
            response_body_recent = response_recent.read()
            recent_dict = ast.literal_eval(response_body_recent.decode('utf-8'))

        win_percent = round(league_dict['wins'] / (league_dict['wins'] + league_dict['losses']) * 100)
        Data.append('\n\n')
        Data.append("{0} \t 레벨: {1} \t 승리: {2} \t 승률: {3}% \t".format(summoner_dict['name'], summoner_dict['summonerLevel'], league_dict['wins'], win_percent))
        Data.append('\n')
        Data.append("티어: {0} \t {1} \t {2}LP".format(league_dict['tier'], league_dict['leaguePoints'], league_dict['tier']))
        Data.append('\n')
        Data.append("\n\t\t\t\t\t\t\t[최근전적]\n\n")

        if(recent_dict['endIndex'] > 5):
            end_index = 5
        else:
            end_index = recent_dict['endIndex']

        for count in range(recent_dict['startIndex'], end_index):
            # 사용 챔피언 검색
            recent_champ = recent_dict['matches'][count]['champion']
            response_champion = urllib.request.urlopen((REGION_ENDPOINT + "/lol/static-data/v3/champions/{0}?&api_key={1}").format(recent_champ, KEY))
            rescode_champion = response_champion.getcode()

            if (rescode_champion == 200):
                response_body_champion = response_champion.read()
                champion1_dict = ast.literal_eval(response_body_champion.decode('utf-8'))

            recent_matches = recent_dict['matches'][count]['gameId']
            response_matches = urllib.request.urlopen((REGION_ENDPOINT + "/lol/match/v3/matches/{0}?&api_key={1}").format(recent_matches, KEY))
            rescode_matches = response_matches.getcode()

            if (rescode_matches == 200):
                response_body_matches = response_matches.read()
                matches_str = response_body_matches.decode('utf-8')
                matches_dict = json.loads(matches_str)
            else:
                break

            minute_playtime = matches_dict['gameDuration'] // 60
            second_playtime = matches_dict['gameDuration'] % 60

            for i in range(0, len(matches_dict['participantIdentities'])):
                if(matches_dict['participants'][i]['championId'] == recent_dict['matches'][count]['champion']):
                    participants_num = i

            if matches_dict['participants'][participants_num]['stats']['win']:
                result = "승리"
            else:
                result = "패배"

            gameStart = matches_dict['gameCreation'] / 1000
            local_tuple = localtime(gameStart)
            time_format = '%Y-%m-%d %H:%M:%S'
            time_str = strftime(time_format, local_tuple)
            Data.append('\n')
            Data.append("★ GAME {0} \t\t {1}! \n   게임시작시간: {2}".format(count + 1, result, time_str))
            Data.append('\n')
            Data.append("   챔피언: {0} \t 포지션: {1} \n   kills: {2} \t deaths: {3} \t assists: {4}".format(champion1_dict['name'], recent_dict['matches'][count]['lane'], matches_dict['participants'][participants_num]['stats']['kills'], matches_dict['participants'][participants_num]['stats']['deaths'], matches_dict['participants'][participants_num]['stats']['assists']))
            Data.append('\n')
            Data.append("   게임 진행 시간: {0} 분 {1} 초 \n   데미지 총량: {2} \t 수집한 골드: {3}G\n".format(minute_playtime, second_playtime, matches_dict['participants'][participants_num]['stats']['totalDamageDealt'], matches_dict['participants'][participants_num]['stats']['goldSpent']))

    return Data
