from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

from config.config import API_KEY
from config.config import API_SECRET

trading_client = TradingClient(API_KEY, API_SECRET, paper=True)

# Get our account information.
account = trading_client.get_account()

print(f"my account: \n{account}")

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print(f"${account.buying_power} is available as buying power.")

# search for US equities
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

#assets = trading_client.get_all_assets(search_params)

# search for AAPL
aapl_asset = trading_client.get_asset('AAPL')

if aapl_asset.tradable:
    #print('We can trade AAPL.')
    pass