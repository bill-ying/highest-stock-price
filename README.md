# highest-stock-price

This program retrieves the highest closing price of a security within a period.

The program depends on package "requests".

To run the program:
- python highest_stock_price.py ticker start_date(YYYY-MM-DD) [optional_end_date(YYYY-MM-DD)]

The security can be listed in New York, London, or Toronto:
- New York listed security, use ticker directly (e.g. AAPL)
- London listed security, use ticker.LON (e.g. BARC.LON)
- Toronto listed security, use ticker.TO (e.g. SU.TO)
