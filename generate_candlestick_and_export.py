## Run technical analysis and pattern analysis on historical data
## Requires talib installation to run
# Export chart data to csv.
import os
import zipfile
import time
import finplot as fplt
import numpy as np
import pandas as pd
import cbpro
import talib

public_client = cbpro.PublicClient()
acceptedGrans = {
    "1m": 60,
    "5m": 300,
    "15m": 900,
    "1h": 3600,
    "6h": 21600,
    "1d": 86400
}

ids = input("Please enter product id(s), comma separated: ")
start = input("Start date in yyyy-mm-dd format: ")
end = input("End date in yyyy-mm-dd format: ")
granularity = input("Enter timeframe: [1m,5m,15m,1h,6h,1d]")

# ids="ETH-BTC,LINK-ETH"
# start ="2021-01-01"
# end = "2021-06-01"
# granularity= "1d"

gran = acceptedGrans[str(granularity)]

product_ids_to_add = ids.split(",")

ohlcv_dictonary = {}
for product_id in product_ids_to_add:
    ohlcv = public_client.get_product_historic_rates(product_id, start, end,
                                                     gran)
    df = pd.DataFrame(
        ohlcv, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
    # create two axes
    ax, ax2 = fplt.create_plot(product_id, rows=2)

    # plot candle sticks
    candles = df[['time', 'open', 'close', 'high', 'low']]
    fplt.candlestick_ochl(candles, ax=ax)

    #Plot volume
    volumes = df[['time', 'open', 'close', 'volume']]
    fplt.volume_ocv(volumes, ax=ax.overlay())

    ohlcv_dictonary[str(product_id)] = ohlcv
    time.sleep(
        1
    )  # Don't want to send too many requests at a time to the public coinbase api

fplt.show()


if not os.path.exists('output'):
    os.makedirs('output')



zipname = ids + "_from_" + start + "_to_" + end + ".zip"
with zipfile.ZipFile("output/" + zipname, 'w') as csv_zip:
    for key in ohlcv_dictonary:
        dataframe_to_write = ohlcv_dictonary[str(key)]
        print(key)
        csv_zip.writestr(key + ".csv", dataframe_to_write.to_csv())
