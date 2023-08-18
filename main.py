from data import binance
from pathlib import Path


# Define the symbol and intervals DATA COLLECTOR
pair = "BTCUSDT"
interval = "5m"
limit = 1000
file_name = 'BTCUSDT_5m_20230701_20230701.csv'
date_start = '2023-07-01 03:00:00'
end_time = '2023-07-04 03:00:00'

exchanger = binance



data = exchanger.fetch_historical_data(pair, interval, limit, date_start, end_time)
file_path = Path('/home/vel/PycharmProjects/data_crypto_collector/', file_name)
data.to_csv(file_path, index=False)
print(f"File {file_name} successfully saved!!! ")
