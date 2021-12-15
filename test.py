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

#load json object

def getVilles():
    with open('city.list.json') as f:
        d = json.load(f)
        villes=pd.DataFrame(d)
        return villes

villes=getVilles()

df = villes[villes["country"]=="FR"]
cityid =df.values


print(cityid)
