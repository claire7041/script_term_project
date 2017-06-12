#import os
#import sys

import urllib.request

import json
"""
https://kr.api.pvp.net/api/lol/kr/.../?api_key=RGAPI-bb875549-7272-48f0-b9e4-2828cdbb6356
"""

REGION_ENDPOINT = "https://kr.api.riotgames.com"
KEY = "RGAPI-bb875549-7272-48f0-b9e4-2828cdbb6356"

# 아이템 리스트
response_current_game = urllib.request.urlopen((REGION_ENDPOINT + "/lol/spectator/v3/featured-games?&api_key={0}").format(KEY))
rescode_current_game = response_current_game.getcode()

if (rescode_current_game == 200):
    response_body_item = response_current_game.read()
    print(response_body_item.decode('utf-8'))
else:
    print("Error Code: " + rescode_current_game)

from time import localtime, strftime

timestamp = 1496236536.737

now = timestamp
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)

print(time_str)

recently_ID = ["2", "2", "3", "4", "5", "7"]





print(recently_ID)

for l in recently_ID:
    print(l)