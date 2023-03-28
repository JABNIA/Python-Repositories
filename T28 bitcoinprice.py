import sys
import requests

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    elif sys.argv[1].isnumeric():
        request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        price = request.json()['bpi']['USD']["rate_float"]
        bitcoin_price = float(sys.argv[1]) * price
        print(f"${bitcoin_price:,.4f}")
       

except requests.RequestException:
    ...
