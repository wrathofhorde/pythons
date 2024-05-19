import sys
import json
import keys

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print('python3 balance.py deposit_amount json_file')
    print('python3 balance.py 100000 owns.json')
    exit(0)
# with open("stocks.json") as s:
#   stocks = json.load(s)
# snp = stocks[0];
# print(json.dumps(snp, indent=2, ensure_ascii=False))

deposit = int(sys.argv[1])
json_file = sys.argv[2]

print("*******************************************")
print(f"입금금액: {format(deposit, ',')}, json file: {json_file}")

with open(json_file) as s:
  stocks = json.load(s)

sum = 0
total_ratio = 0

for s in stocks:
  total_ratio += s[keys.RATIO]

for s in stocks:
  s[keys.TOTAL_PRICE] = s[keys.UNIT_PRICE] * s[keys.QUANTITY]
  s[keys.PERCENT] = round(s[keys.RATIO] / total_ratio, 2)
  sum += s[keys.TOTAL_PRICE]

sum += deposit  #주식 가격에 입금액 추가

for s in stocks:
  s[keys.ASSIGNMENT] = round(sum * s[keys.PERCENT]) - s[keys.TOTAL_PRICE]
  s[keys.ASSIGNMENT] = s[keys.ASSIGNMENT] if s[keys.ASSIGNMENT] >= s[keys.UNIT_PRICE] else 0
  s[keys.BUY] = s[keys.ASSIGNMENT] // s[keys.UNIT_PRICE]

total_price_to_buy = 0

for s in stocks:
  total_price_to_buy += s[keys.BUY] * s[keys.UNIT_PRICE]

balance = deposit - total_price_to_buy

for s in stocks:
  if s[keys.BUY] == 0 and balance > s[keys.UNIT_PRICE]:
    extra_buy = balance // s[keys.UNIT_PRICE]
    s[keys.BUY] += extra_buy
    balance -= extra_buy * s[keys.UNIT_PRICE]

total_balance = 0

for s in stocks:
  s[keys.BALANCE_AFTER_BUY] = s[keys.BUY] * s[keys.UNIT_PRICE] + s[keys.TOTAL_PRICE]
  total_balance += s[keys.BALANCE_AFTER_BUY]

out_json =[]

for s in stocks:
  s[keys.RATIO_AFTER_BUY] = round(100 * s[keys.BALANCE_AFTER_BUY] / total_balance, 1)
  j = json.dumps(s, indent = 2, ensure_ascii = False)
  out_json.append(s)
  print(j)

with open("out.json", 'w', encoding="utf-8") as w:
  json.dump(out_json, w, ensure_ascii = False, indent = 2)

for s in stocks:
  print(f"{s[keys.NAME]}: {s[keys.BUY]}, {s[keys.RATIO_AFTER_BUY]}%")

print(f"잔액: {balance}")
