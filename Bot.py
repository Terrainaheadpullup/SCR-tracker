import json
import time
import csv
from datetime import datetime
import os
from urllib.request import urlopen

for i in range(10000000000):

    with urlopen('https://api.wheretheiss.at/v1/satellites/25544') as response:
        source2 = response.read()
        data2 = json.loads(source2)
        print(data2)

    now = datetime.now()
    dt = now.strftime('%Y-%m-%d %H:%M:%S')

    item = data2['latitude']
    item2 = data2['longitude']
    item3 = data2['altitude']
    item4 = data2['velocity']
    f = open(r'C:\Users\Flynn\Documents\GitHub\SCR-tracker\SCR Tracker.csv', 'a', encoding='utf-8' ,newline='')
    thewriter = csv.writer(f) 
    thewriter.writerow([dt, item, item2, item3, item4])
    time.sleep(1)
close(f)

