# import os
# import csv

# def WriteCSV(data):
#     pathFileCsv = os.path.isfile('./weatherOpenMap.csv')

#     if pathFileCsv == False:
#         with open('weatherOpenMap.csv', 'w') as fw:  # Just use 'w' mode in 3.x
#             w = csv.DictWriter(fw, data.keys())
#             w.writeheader()
#             w.writerow(data)

#     else:
#         with open('weatherOpenMap.csv', 'a') as fa:
#             w = csv.DictWriter(fa, data.keys())
#             w.writerow(data)

# val = {'city': 'Forville', 'country': 'FR', 'temp': 2.73, 'temp_max': 4.54, 'temp_min': -4.63, 'humidity': 61, 'pressure': 1032, 'sky': 'Clouds', 'sunrise': '08:03 AM', 'sunset': '04:52 PM', 'wind': 1.84, 'wind_deg': None, 'dt': '08:11 PM', 'cloudiness': 54}
# WriteCSV(val)


import pandas as pd
import json 
import pandas as pd 
from pandas.io.json import json_normalize #package for flattening json in pandas df
import urllib.request

#load json object

# def getVilles():
#     with open('city.list.json') as f:
#         d = json.load(f)
#         villes=pd.DataFrame(d)
#         return villes

# villes=getVilles()

# df = villes[villes["country"]=="FR"]
# cityid =df.values


# print(cityid)

def data_fetch(full_api_url):

    print(full_api_url)
    url = urllib.request.urlopen(full_api_url)
    print(f"url : {url}")
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    print(raw_api_dict) 


data_fetch("http://api.openweathermap.org/data/2.5/weather?q=Mons-en-Bar%C5%93ul,FR&mode=json&units=metric&APPID=ac756dbda4be086b798c4302361463a5")