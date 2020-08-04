import json
import time
from datetime import datetime
import gspread
import os
from urllib.request import urlopen
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('SheetConnection.json', scope)

client = gspread.authorize(creds)

sheet2 = client.open('SCR Tracker 3').sheet1

B = 2

for i in range(10000000000):

    with urlopen('https://games.roblox.com/v1/games?universeIds=300039023') as response:
        source2 = response.read()
        data2 = json.loads(source2)

    file = open(r'C:\Users\Flynn\Documents\Python\dump2.json', 'w', encoding='utf-8')
    json.dump(data2, file, ensure_ascii=False, indent=2)
    file.close()

    now = datetime.now()
    dt = now.strftime('%Y-%m-%d %H:%M:%S')

    file = open(r'C:\Users\Flynn\Documents\Python\dump2.json', 'r', encoding='utf-8')
    text2 = json.load(file)
    file.close()
    print(text2)

    for objects in text2['data']:
        Count2 = objects['playing']
        sheet2.update_cell(B,2, Count2)
    sheet2.update_cell(B,1, dt)
    B=B+1
    time.sleep(120)


