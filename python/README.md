# ks_api_client
No description provided

- API version: 1.0.1
- Package version: 1.1.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install -e "git+https://github.com/paramatrixtech/ksapi.git#egg=ks_api_client&subdirectory=./python"
```
(you may need to run `pip` with root permission: `sudo pip install -e "git+https://github.com/paramatrixtech/ksapi.git#egg=ks_api_client&subdirectory=./python"`)

Then import the package:
```python
import ks_api_client
```

### Settings configurations:
- Add your configuration in settings.py file or create "settings_file" environment variable with your settings.py file path e.g. settings_file=/etc/ksapi/settings.py (for linux) or settings_file=C:\\\Users\\\ksapi\\\Desktop\\\settings.py (for Windows).
- Add all the required parameters in the settings.py file, then no need to pass those paramaters during KSTradeApi object creation.


### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ks_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then refer to the sample code below for various API requests:

```python
from ks_api_client import ks_api
# Defining the host is optional and defaults to https://sbx.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.
client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "test", \
                        host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = "")
					 
# Initiate login and generate OTT
client.login(password = "")

#Complete login and generate session token
client.session_2fa()
#You can choose to use a day-to-day access code by adding accesscode parameter : client.session_2fa(access_code = "")

# Place an order. 
# Order_type can be "N", "MIS", "MTF". "SOR". Set variety as "AMO" for post-market orders. 
# Please check detailed documentation (see bottom of page) for more details on each variable. 
# Instrument tokens can be found at the following urls (NOTE: Please replace DD_MM_YYYY with the latest date for updated instrument tokens, for example 27_05_2021 will give tokens for 27 may):
# Equity: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_DD_MM_YYYY.txt
# Derivatives: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_DD_MM_YYYY.txt
client.place_order(order_type = "N", instrument_token = 727, transaction_type = "BUY",\
                   quantity = 1, price = 0, disclosed_quantity = 0, trigger_price = 0,\
                   tag = "string", validity = "GFD", variety = "REGULAR")
						
# Modify an order
client.modify_order(order_id = "", price = 0, quantity = 1, disclosed_quantity = 0, trigger_price = 0, validity = "GFD")

# Cancel an order
client.cancel_order(order_id = "")

# Get Order Book
client.order_report()

# Get Detailed Order Report for specific order id [equity] . 
client.order_report(order_id = "")

# Get Detailed Order Report for specific order id [FNO] .
client.order_report(order_id = "", is_fno = "Y")

# Get Trade Book
client.trade_report()

# Get Detailed Trade Report for specific order id [equity] . 
client.trade_report(order_id = "")

# Get Detailed Trade Report for specific order id [FNO] .
client.trade_report(order_id = "", is_fno = "Y")

# Get Margin required for Equity orders. 
order_info = [
    {"instrument_token": 727, "quantity": 1, "price": 1300, "amount": 0, "trigger_price": 1190},
    {"instrument_token": 1374, "quantity": 1, "price": 1200, "amount": 0, "trigger_price": 1150}
]
client.margin_required(transaction_type = "BUY",order_info = order_info)

# Get Available Margin
client.margin()

# Get Positions. position_type can be "TODAYS", "OPEN", "STOCKS".
client.positions(position_type = "TODAYS")

# Get Quote details. 
client.quote(instrument_token = "110")
# Get Quotes for multiple tokens at once. Separate tokens by a hyphen. 
client.quote(instrument_token = "727-1250")


# Websocket: 

# Subscribe to instrument price feed:
def callback_method(message):
    print(message)
    print("Your logic/computation will come here.")
client.subscribe(input_tokens="745,754", callback=callback_method)
# Response structure: 
# ignore, ignore, Best buy price, Best buy quantity, Best sell price, Best sell quantity, Last trade price, High price, Low price, 
# Average trade price, Closing price, Open price, Net change percentage, Total sell quantity, Total buy quantity, Total trade qty, 
# Open Interest, Total trade value, Last trade quantity, Last trade time, Net change, Upper circuit limit, Lower circuit limit

# Subscribe to order status update websocket
# (instrument token supplied in function is merely a placeholder and serves no purpose here): 
def callback_method(message):
    print(message)
    print("Your logic/computation will come here.")
client.subscribe(input_tokens="727", callback=callback_method, broadcast_host="https://wstreamer.kotaksecurities.com/feed/orders")


# Unsubscribe from streaming service.
client.unsubscribe()

#Terminate user's Session
client.logout()
```
## Documentation for API Endpoints

All URIs are relative to "host" parameter

Class | Method | Description
------------ | ------------- | -------------
*SessionApi* | [**ks_api.KSTradeApi**](docs/SessionApi.md#session_init) | Initialise Session
*SessionApi* | [**login**](docs/SessionApi.md#login) | Login using Userid
*SessionApi* | [**session_2fa**](docs/SessionApi.md#session_2fa) | Generate final Session Token
*OrderApi* | [**place_order**](docs/OrderApi.md#place_order) | Place a New order
*OrderApi* | [**modify_order**](docs/OrderApi.md#modify_order) | Modify an existing order
*OrderApi* | [**cancel_order**](docs/OrderApi.md#cancel_order) | Cancel an order
*ReportsApi* | [**order_report**](docs/ReportsApi.md#order_report) | Get order report
*ReportsApi* | [**trade_report**](docs/ReportsApi.md#trade_report) | Get trade report
*MarginApi* | [**margin_required**](docs/MarginApi.md#margin_required) | Get Margin Required for an order by amount or quantity.
*MarginApi* | [**margin**](docs/MarginApi.md#margin) | Get all calculated margins.
*PositionsApi* | [**positions**](docs/PositionsApi.md#positions) | Get&#39;s Open position.
*QuoteApi* | [**quote**](docs/QuoteApi.md#quote_details) | Get Quote details
*StreamingApi* | [**subscribe**](docs/StreamingApi.md#subscribe) | Subscribe to streaming api of specified instrument tokens.
*StreamingApi* | [**unsubscribe**](docs/StreamingApi.md#unsubscribe) | Unsubscribe from streaming api.
*SessionApi* | [**logout**](docs/SessionApi.md#logout) | Invalidate Session Token


