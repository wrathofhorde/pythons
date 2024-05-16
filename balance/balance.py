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

print(f"{snp[keys.NAME]}: {snp[keys.BUY]}")
print(f"{qqq[keys.NAME]}: {qqq[keys.BUY]}")
print(f"{n50[keys.NAME]}: {n50[keys.BUY]}")

