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
- Add your configuration in settings.py file or create "settings_file" environment variable with your settings.py file path (e.g. settings_path=/etc/ksapi/settings.py).
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

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from ks_api_client import ks_api
# Defining the host is optional and defaults to https://sbx.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.
client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "", \
                        host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = "")
					 
# Initiate login and generate OTT
client.login(password = "")

#Complete login and generate session token
client.session_2fa()
#You can choose to use a day-to-day access code by adding accesscode parameter : client.session_2fa(access_code = "")

# Place an order                   
client.place_order(order_type = "N", instrument_token = 727, transaction_type = "BUY",\
                   quantity = 1, price = 0, disclosed_quantity = 0, trigger_price = 0,\
                   tag = "string", validity = "GFD", variety = "REGULAR")
						
# Modify an order
client.modify_order(order_id = "", price = 0, quantity = 1, disclosed_quantity = 0, trigger_price = 0, validity = "GFD")

# Cancel an order
client.cancel_order(order_id = "")

# Get Report Orders
client.order_report()

# Get Report Orders for order id
client.order_report(order_id = "")

# Get FNO Report Orders for order id
client.order_report(order_id = "", is_fno = "Y")

# Get Trade Report
client.trade_report()

# Get Trade Report for order id
client.trade_report(order_id = "")

# Get FNO Trade Report for order id
client.trade_report(order_id = "", is_fno = "Y")

# Get Margin required
order_info = [
    {"instrument_token": 727, "quantity": 1, "price": 1300, "amount": 0, "trigger_price": 1190},
    {"instrument_token": 1374, "quantity": 1, "price": 1200, "amount": 0, "trigger_price": 1150}
]
client.margin_required(transaction_type = "BUY",order_info = order_info)

# Get Margin
client.margin()

# Get Positions
client.positions(position_type = "TODAYS")

# Get Quote details
client.quote(instrument_token = 110)

# Subscribe to instrument token's stream.
def callback_method(message):
    print(message)
    print("Your logic/computation will come here.")
client.subscribe(input_tokens="745,754", callback=callback_method)

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


