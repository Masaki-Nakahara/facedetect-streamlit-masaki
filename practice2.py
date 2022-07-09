import requests
import json
import pprint

url = 'https://zipcloud.ibsnet.co.jp/api/search'

params = {'zipcode':'2330007'}

res = requests.get(url, params=params)

data = json.loads(res.text)
pprint.pprint(data)