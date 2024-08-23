import duration
import handledic
import closingprice
from icecream import ic
from datetime import timedelta

days = duration.days()
prices = handledic.read()
yesterday = days.yesterday
firstday = days.firstday
startday = days.startday
endday = days.endday
diff = yesterday - startday

for offset in range(diff.days):
    day = days.tostring(startday + timedelta(days=offset))

    if prices.get(day) is None:
        list = closingprice.get(day)
        prices[day] = list
        print(f"{day}: {list}")
    else:
        print(f"{day} skipped")

handledic.write(prices)