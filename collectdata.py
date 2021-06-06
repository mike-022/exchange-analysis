# REST API
# For Public Endpoints, our rate limit is 3 requests per second, up to 6 requests per second in bursts. For Private Endpoints, our rate limit is 5 requests per second, up to 10 requests per second in bursts.

# FIX API
# The FIX API rate limit is 50 messages per second. More information about our rate limits can be found here.
import cbpro2
public_client = cbpro2.PublicClient()


products = public_client.get_products()
print(products)

# Get the order book at the default level.
public_client.get_product_order_book('BTC-USD')
# Get the order book at a specific level.
public_client.get_product_order_book('BTC-USD', level=1)