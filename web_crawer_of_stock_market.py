import requests
from bs4 import BeautifulSoup
import time
stock = 0
dates = 0
def check_date(dates):
  if len(dates) < 8 or len(dates) > 8:
    print("Must have 8 elements!")
    return "N"
  if not dates.isdigit():
    print("Must be numbers!")
    return "N"
  else:
    return "Y"

print("Please enter the number you want to see the number of stock. Ex:2330")
stock = input()
print("Please enter the year and date you want to see the number of stock. Ex:20200101")
dates = input()
check_date(dates)
for d in check_date(dates):
  print(d)
  if d == "N":
    break
  else:
    stock1 = stock
    dates = int(dates)
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}'
    resstock = requests.get(url.format(dates,stock1))#get資料
    time.sleep(5)
    print("Done")
    resstock.raise_for_status()
    soupstock = BeautifulSoup(resstock.text, 'html.parser')
    tablestock = soupstock.find_all('tr')
    for trstock in tablestock:
        tdstock = trstock.find_all('td')
        if len(tdstock) < 1:
            continue
        ystock = [a.text.strip() for a in tdstock if a.text.strip()]
        print(ystock[0],ystock[1],ystock[2],ystock[3],ystock[4],ystock[5],ystock[6])
