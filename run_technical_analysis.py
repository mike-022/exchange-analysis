## Run technical analysis and pattern analysis on historical data
## Requires talib installation to run
## Adding a few basic indicators for the sake of test but can easily add more

import time
import numpy as np
import pandas as pd
import cbpro
import talib
import datetime
import utils.validator as v

public_client = cbpro.PublicClient()
acceptedGrans = {"1m":60,"5m":300,"15m":900,"1h":3600,"6h":21600,"1d":86400}


# For the sake of simplicity we will fail over if the requested data set is too big.
# For an enhanced product, including if we  
ids = input("Please enter product id(s), comma separated i.e.'ETH-BTC,LINK-ETH': ")
start = input("Start date in yyyy-mm-dd format: ")
end = input("End date in yyyy-mm-dd format: ")
granularity = input("Enter timeframe: [1m,5m,15m,1h,6h,1d]: ")

#Hardcoded
# ids="ETH-BTC,LINK-ETH"
# start ="2021-01-01"
# end = "2021-06-01"
# granularity= "1d"


gran = acceptedGrans[str(granularity)]

product_ids_to_add = ids.split(",")

# Creating a dictionary for future comparisons of data streams
ohlcv_dictonary = {}
for product_id in product_ids_to_add:
    ohlcv = public_client.get_product_historic_rates(product_id,start,end,gran)
    df = pd.DataFrame(ohlcv, columns = ['time', 'low','high','open','close','volume']) 

    ohlcv_dictonary[str(product_id)]= df

    #DOJI Technical pattern
    CDL3BLACKCROWS = talib.CDL3BLACKCROWS(df['open'], df['high'], df['low'], df['close'])
    MFI = talib.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod=14)
    doji = talib.CDLDOJI(df['open'], df['high'], df['low'], df['close'])
    ohlcv_dictonary[str(product_id)]["doji_count"] = doji[doji!=0].size
    print(product_id + " has " + str(doji[doji!=0].size) + " doji candles from " + start + " to " + end + " on the " + granularity + "."  )

    #Cycle indicator
    real = talib.HT_DCPHASE(df['close'])
    print(product_id + " has " + str(real[real>100].size) + " candles above 250 hilbert dominant phase from " + start + " to " + end + " on the " + granularity + "."  )

    #Volume indicators
    onbalancevolume = talib.OBV(df['close'], df['volume'])
    chaikinadoscillator = talib.ADOSC(df['high'], df['low'], df['close'], df['volume'], fastperiod=3, slowperiod=10)
    
    

    time.sleep(1)# Don't want to send too many requests at a time to the public coinbase api




