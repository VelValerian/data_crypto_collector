from data import binance
from datetime import datetime as date

# Define the symbol and intervals DATA COLLECTOR
pair = "BTCUSDT"
interval = "5m"
limit = 1000
file_name = 'BTCUSDT_5m_20230701'
date_start = '2023-07-01 03:00:00'


now = date.now()
current_date = now.strftime('%Y-%m-%d %H:%M:%S')

# Datetime to ms
start_time = int(date.strptime(date_start, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
end_time = int(date.strptime(current_date, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)

data = binance.fetch_historical_data(pair, interval, limit, start_time, end_time)

print(data)
