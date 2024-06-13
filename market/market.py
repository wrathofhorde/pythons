import requests
from icecream import ic
from datetime import datetime
from datetime import timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
date = yesterday.strftime("%Y-%m-%d") + "T09:01:00%2B09:00"

markets = ["KRW-BTC", "KRW-ETH", "KRW-XRP"]
headers = {"accept": "application/json"}
url = "https://api.upbit.com/v1/candles/minutes/1?market=%s&to=%s"


for market in markets:
    print(url % (market, date))
    res = requests.get(url % (market, date), headers=headers)

    if res.status_code == 200:
        data = res.json()
        ic(data)
    else:
        ic(res)
