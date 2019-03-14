
import json, requests

alphaVantageKey = '&apikey=OYAJLARX2ZAA2T1B'
url ="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol="

urlWithTicker = url+'MSFT'+alphaVantageKey
myResponse = requests.get(urlWithTicker)

print(myResponse.content)