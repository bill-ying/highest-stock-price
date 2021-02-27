import argparse
import datetime

import requests

# This is my Alpha Vantage key.  Please register your own Alpha Vantage key and replace with it in the following line
ALPHA_VANTAGE_KEY = 'OYAJLARX2ZAA2T1B'
STOCK_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&apikey=' \
            + ALPHA_VANTAGE_KEY + '&symbol='
CLOSE_PRICE_KEY = '4. close'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retrieve highest closing price of a security between certain dates')
    parser.add_argument('ticker', help='security ticker')
    parser.add_argument('start_date', help='start date in YYYY-MM-DD inclusive')
    parser.add_argument('end_date', nargs='?', default=datetime.datetime.today().strftime('%Y-%m-%d'),
                        help='optional end date in YYYY-MM-DD inclusive (default is current date)')
    args = parser.parse_args()
    stock_response = requests.get(STOCK_URL + args.ticker).json()

    if 'Error Message' in stock_response:
        print('Ticker ' + args.ticker + ' is invalid')
        exit(1001)
    else:
        prices = stock_response['Time Series (Daily)']
        prices_in_dates = {k: v for k, v in prices.items() if args.start_date <= k <= args.end_date}
        date_for_highest_price = max(prices_in_dates, key=lambda x: float(prices_in_dates[x][CLOSE_PRICE_KEY]))
        currency_symbol = '\u00a3' if str(args.ticker).endswith('.LON') else '$'
        print(date_for_highest_price,
              currency_symbol + '{0:.2f}'.format(float(prices_in_dates[date_for_highest_price][CLOSE_PRICE_KEY])))
