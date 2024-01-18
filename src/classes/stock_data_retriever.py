from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockLatestQuoteRequest
from datetime import datetime
import pandas as pd

class StockDataRetriever:

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_latest_price(self, symbol):
        client = StockHistoricalDataClient(self.api_key, self.api_secret)
        request_params = StockLatestQuoteRequest(symbol_or_symbols=symbol)
        latest_quotes = client.get_stock_latest_quote(request_params)
        ask_price = latest_quotes[symbol].ask_price
        return ask_price


    def get_dataframe(self, symbol: str, years_back: int = 3) -> pd.DataFrame:
        client = StockHistoricalDataClient(self.api_key, self.api_secret)
        now = datetime.now()
        request = StockBarsRequest(
            symbol_or_symbols=symbol,
            timeframe= TimeFrame.Day,
            start=datetime((now.year-years_back), now.month, now.day)
        )
        bars = client.get_stock_bars(request_params=request)
        return bars.df

    #print(get_dataframe(API_KEY, API_SECRET, "AAPL")) #works

