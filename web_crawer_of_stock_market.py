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
  if d == "N":
    break
  else:
    stock1 = int(stock)
    dates = int(dates)
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}'
    res2330 = requests.get(url.format(dates,stock1))#get資料
    time.sleep(5)
    print("Done")
    res2330.raise_for_status()
    soup2330 = BeautifulSoup(res2330.text, 'html.parser')
    table2330 = soup2330.find_all('tr')
    for tr2330 in table2330:
        td2330 = tr2330.find_all('td')
        if len(td2330) < 1:
            continue
        y2330 = [a.text.strip() for a in td2330 if a.text.strip()]
        print(y2330[0],y2330[1],y2330[2],y2330[3],y2330[4],y2330[5],y2330[6])
    break
