import keys
import owns

# with open("stocks.json") as s:
#   stocks = json.load(s)

# snp = stocks[0];
# print(json.dumps(snp, indent=2, ensure_ascii=False))


sum = 0
total_ratio = 0
index = owns.index
stocks = owns.owns
deposit = owns.deposit

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

snp = stocks[index[keys.SNP]]
qqq = stocks[index[keys.QQQ]]
n50 = stocks[index[keys.NIFTY_50]]

total_price_to_buy = 0

for s in stocks:
  total_price_to_buy += s[keys.BUY] * s[keys.UNIT_PRICE]

balance = deposit - total_price_to_buy

if balance > n50[keys.UNIT_PRICE]:
  extra_buy = balance // n50[keys.UNIT_PRICE]
  n50[keys.BUY] += extra_buy
  balance -= extra_buy * n50[keys.UNIT_PRICE]

total_balance = 0

for s in stocks:
  s[keys.BALANCE_AFTER_BUY] = s[keys.BUY] * s[keys.UNIT_PRICE] + s[keys.TOTAL_PRICE]
  total_balance += s[keys.BALANCE_AFTER_BUY]

snp_ratio = round(100 * snp[keys.BALANCE_AFTER_BUY] / total_balance, 1)
qqq_ratio = round(100 * qqq[keys.BALANCE_AFTER_BUY] / total_balance, 1)
n50_ratio = round(100 * n50[keys.BALANCE_AFTER_BUY] / total_balance, 1)

print(snp)
print(qqq)
print(n50)

print(f"{snp[keys.NAME]}: {snp[keys.BUY]}, {snp_ratio}%")
print(f"{qqq[keys.NAME]}: {qqq[keys.BUY]}, {qqq_ratio}%")
print(f"{n50[keys.NAME]}: {n50[keys.BUY]}, {n50_ratio}%")

print(f"잔액: {balance}")