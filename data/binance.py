import pandas as pd
from binance.um_futures import UMFutures


def fetch_historical_data(pair, interval, limit, start_time, end_time):
    client = UMFutures()
    klines_df = []
    #
    # while start_time<end_time:

    klines_data = client.continuous_klines(pair=pair, contractType='PERPETUAL', interval=interval,
                                               startTime=start_time, endTime=end_time, limit=limit)

    klines_df += klines_data

    df = pd.DataFrame(klines_df, columns=["timestamp", "open", "high", "low", "close", "volume", "close_time",
                                        "quote_asset_volume", "number_of_trades", "taker_buy_base_asset_volume",
                                        "taker_buy_quote_asset_volume", "ignore"])
    df = df.drop_duplicates()
    return df
