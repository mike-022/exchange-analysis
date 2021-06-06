######## Gather all trading pair tickers ######

import cbpro
# Using public client to retrieve data
public_client = cbpro.PublicClient()
products = public_client.get_products()

by_quote_currency = {}
by_base_currency = {}

for item in products:
    quote_currency = item["quote_currency"]
    if item["quote_currency"] not in by_quote_currency:
        by_quote_currency[str(quote_currency)] = {}
        by_quote_currency[str(quote_currency)]["pairs"] = []
    by_quote_currency[str(quote_currency)]["pairs"].append(item["id"])

    base_currency = item["base_currency"]
    if item["base_currency"] not in by_base_currency:
        by_base_currency[str(base_currency)] = {}
        by_base_currency[str(base_currency)]["pairs"] = []
    by_base_currency[str(base_currency)]["pairs"].append(item["id"])

productids = ""
for key, value in by_base_currency.items():
    productids += key + ": "
    for pair in value["pairs"]:
        productids += pair + ", "
    productids += "\n"

print(productids)