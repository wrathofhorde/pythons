import duration
import handledic
import handlecsv
import closingprice
from datetime import timedelta

days = duration.days()
prices = handledic.read()
today = days.today
firstday = days.firstday
startday = days.startday
endday = days.endday
diff = today - startday

for offset in range(diff.days):
    day = days.tostring(startday + timedelta(days=offset))
    value = prices.get(day)

    if value is None or len(value) != 3:
        list = closingprice.get(day)
        prices[day] = list
        print(f"{day}: {list}")
    else:
        print(f"{day} skipped")

handledic.write(prices)

csvlist = []
btc = eth = xrp = 0
diff = endday - startday
sum_of_days = diff.days + 1

for offset in range(sum_of_days):
    day = days.tostring(startday + timedelta(days=offset))
    value = prices.get(day)
    btc += value[0]
    eth += value[1]
    xrp += value[2]
    value.insert(0, day)
    csvlist.append(value)

btc /= sum_of_days
eth /= sum_of_days
xrp /= sum_of_days
btc = round(btc, 0)
eth = round(eth, 0)
xrp = round(xrp, 0)


str_startday = days.tostring(startday)
str_endday = days.tostring(endday)

handlecsv.write(csvlist)

print(f"{str_startday} ~ {str_endday} 1년({sum_of_days}일) BTC 종가 평균:{int(btc)}")
print(f"{str_startday} ~ {str_endday} 1년({sum_of_days}일) ETH 종가 평균:{int(eth)}")
print(f"{str_startday} ~ {str_endday} 1년({sum_of_days}일) XRP 종가 평균:{int(xrp)}")

