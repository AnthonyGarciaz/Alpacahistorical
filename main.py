import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame

# Load environment variables from .env file
load_dotenv()

# Retrieve the API keys from environment variables
api_key = os.getenv('APCA_API_KEY_ID')
api_secret = os.getenv('APCA_API_SECRET_KEY')

# Set up the API
api = tradeapi.REST(api_key, api_secret, base_url='https://paper-api.alpaca.markets')

# Specify the ticker, timeframe, and date range
symbol = 'TSLA'
timeframe = TimeFrame.Day  # Daily data
start_date = '2015-01-01'  # Adjusted format
end_date = '2023-12-31'    # Adjusted format

# Get the historical data
data = api.get_bars(symbol, timeframe, start=start_date, end=end_date).df

# Display the data
print(data.head())
