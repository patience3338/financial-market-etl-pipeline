import requests
import pandas as pd
from sqlalchemy import create_engine

# Stock API
API_KEY = "UWS0Q8T4EYLGA0MX"
symbol = "ALV.DE"

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

response = requests.get(url)
stock_data = response.json()

# Transform data
time_series = stock_data['Time Series (Daily)']

df = pd.DataFrame.from_dict(time_series, orient='index')
df.columns = ['open', 'high', 'low', 'close', 'volume']

df.index = pd.to_datetime(df.index)
df = df.astype(float)
df = df.sort_index()

# Feature Engineering
df.dropna(inplace=True)
df['daily_return'] = df['close'].pct_change()
df['volatility'] = df['daily_return'].rolling(7).std()

# PostgreSQL connection
engine = create_engine('postgresql://postgres:5678@localhost:5432/financial_db')

df.to_sql('market_prices', engine, if_exists='replace')

print("✅ Pipeline executed successfully")