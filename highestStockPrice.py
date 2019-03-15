
import json, sys
import requests

alphaVantageKey = '&apikey=OYAJLARX2ZAA2T1B'
url ="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol="

if len(sys.argv) == 1:
    print("Usage: highestStockPrice ticker YYYY-MM-DD YYYY-MM-DD")
else:
    urlWithTicker = url+sys.argv[1]+alphaVantageKey
    myResponse = requests.get(urlWithTicker)
    jsonData = myResponse.json()
    key = list(jsonData)[1]
    prices = jsonData[key]
    pricesInDates = {k: v for k, v in prices.items() if k >= sys.argv[2] and k <= sys.argv[3]}
    dateKey = max(pricesInDates, key=lambda x: float(pricesInDates[x]['4. close']))
    print(dateKey, "${0:.2f}".format(float(pricesInDates[dateKey]['4. close'])))