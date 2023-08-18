from data import binance


# Define the symbol and intervals DATA COLLECTOR
pair = "BTCUSDT"
interval = "5m"
limit = 1000
file_name = 'BTCUSDT_5m_20230701'
date_start = '2023-07-01 03:00:00'
end_time = None





data = binance.fetch_historical_data(pair, interval, limit, date_start, end_time)

print(data)
