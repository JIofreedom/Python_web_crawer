import requests
from bs4 import BeautifulSoup
import time
stock = 0
dates = 0
day = [] #for day1
day1 = [] #for X axis
op = [] #opening price
H = [] #highest price
L = [] #lowest price
cl = [] #close price
def check_date(dates):#check the input of the date 
  if len(dates) < 6 or len(dates) > 6:
    print("Must have 8 elements!")
    return "N"
  if not dates.isdigit():
    print("Must be numbers!")
    return "N"
  else:
    return "Y"

print("Please enter the number you want to see of stock. Ex:'2330' for tsmc please enter '2330'")
stock = input()
print("Please enter the year and date you want to see the number of stock. Ex:For 2021/01 please enter 202101")
dates = input()
check_date(dates)
for d in check_date(dates):
  if d == "N":
    break
  else:
    stock1 = stock
    dates = int(dates)
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}'
    resstock = requests.get(url.format(dates,stock1))#get data from the website(url)
    time.sleep(5)#sleep for 5s
    resstock.raise_for_status()
    soupstock = BeautifulSoup(resstock.text, 'html.parser')
    tablestock = soupstock.find_all('tr')
    for trstock in tablestock:
        tdstock = trstock.find_all('td')
        if len(tdstock) < 1:
            continue
        ystock = [a.text.strip() for a in tdstock if a.text.strip()]
        print(ystock[0],ystock[1],ystock[2],ystock[3],ystock[4],ystock[5],ystock[6])
    print("Done")
#Below is a line chart of the stock market
import matplotlib.pyplot as plt
import numpy as np
del day[0] #delete the head of the list because it's not the value I need
del op[0]
del H[0]
del L[0]
del cl[0]
i = 0
while i < len(day):
    day1.append(day[i][7:10])
    i = i + 1
day1 = [(int(x)) for x in day1]
op = [(float (x)) for x in op]
H = [(float (x)) for x in H]
L = [(float (x)) for x in L]
cl = [(float (x)) for x in cl]
plt.plot(day1,op,'.-',color='black')
plt.plot(day1,H,'.-',color='red')
plt.plot(day1,L,'.-',color='green')
plt.plot(day1,cl,'.-',color='blue')
plt.xticks(np.arange(day1[0],day1[-1],1.0))
plt.yticks(np.arange(min(L)-5,max(H)+5,5.0))
plt.title(stock +'stock this month')
plt.xlabel('Day')
plt.ylabel('Dollars(NTD.)')
plt.legend(['Opening Price','Highest Price','Lowest Price','Close Prise'])
plt.grid(True)
plt.show()
