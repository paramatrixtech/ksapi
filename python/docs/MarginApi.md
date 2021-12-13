# ks_api_client.MarginApi

All URIs are relative to *https://tradeapi.kotaksecurities.com/apim*

Method | Description
------------- | -------------
[**margin_required**](MarginApi.md#margin_required) | Get Margin Required for an order by amount or quantity.
[**get_margins**](MarginApi.md#get_margins) | Gives complete Margin Details of a Client from RMS.


# **margin_required**
> object margin_required(transaction_type, order_info)

Get Margin Required for an order by amount or quantity.

Returns margin required for Equity, Super Multiple & MTF Order.

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                 consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

#First initialize session and generate session token

try:
    # Get Margin Required for an order by amount or quantity.
        order_info = [
            {"instrument_token": 727, "quantity": 1, "price": 1300, "amount": 0, "trigger_price": 1190},
            {"instrument_token": 1374, "quantity": 1, "price": 1200, "amount": 0, "trigger_price": 1150}
        ]
    client.margin_required(transaction_type="BUY",order_info=order_info)
except Exception as e:
    print("Exception when calling MarginApi->margin_required: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**transaction_type** | **str** | Transaction Type - BUY or SELL | 
**order_info** | [**list[OrderInfo]**](OrderInfo.md) |  | 

### Return type

**object**

### Sample response
```python
{
  "Success": [
    {
      "instrumentToken": 727,
      "mtf": 325,
      "normal": 260,
      "superMultiple": 227
    },
    {
      "instrumentToken": 1374,
      "mtf": 0,
      "normal": 240,
      "superMultiple": 99.2
    }
  ]
}

```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the Margin required by client for order. |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

# **get_margins**
> object get_margins()

Get complete Margin details.

Returns complete margin details for Equity, Super Multiple & MTF Order.

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                 consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

#First initialize session and generate session token

try:
    # Get Margin details.
    client.get_margins()
except Exception as e:
    print("Exception when calling MarginApi->margin_required: %s\n" % e)
```

### Return type

**object**

### Sample response
```python
{
  "Success": {
    "commodities": [],
    "currency": [
      {
        "exchange": "NSE",
        "futures": {
          "additionalOptionBrokerage": 0,
          "availableCashBalance": 999999999,
          "clientGroupLimit": 0,
          "debtorFlag": 0,
          "dtv": 0,
          "dtvBTSTSell": 0,
          "initialMargin": 0,
          "marginAvailable": 999999572.4,
          "marginUtilised": 426.6,
          "mfLien": 0,
          "mtm": 0,
          "nriPinsBalance": 0,
          "optionPremium": 0,
          "realizedPL": 0,
          "securityMargin": 0,
          "totalMargin": 999999999
        },
        "options": {
          "additionalOptionBrokerage": 0,
          "availableCashBalance": 999999999,
          "clientGroupLimit": 0,
          "debtorFlag": 0,
          "dtv": 0,
          "dtvBTSTSell": 0,
          "initialMargin": 0,
          "marginAvailable": 999999572.4,
          "marginUtilised": 426.6,
          "mfLien": 0,
          "mtm": 0,
          "nriPinsBalance": 0,
          "optionPremium": 0,
          "realizedPL": 0,
          "securityMargin": 0,
          "totalMargin": 999999999
        }
      }
    ],
    "derivatives": [
      {
        "exchange": "NSE",
        "futures": {
          "additionalOptionBrokerage": 0,
          "availableCashBalance": 999999999,
          "clientGroupLimit": 0,
          "debtorFlag": 0,
          "dtv": 0,
          "dtvBTSTSell": 0,
          "initialMargin": 0,
          "marginAvailable": 999999572.4,
          "marginUtilised": 426.6,
          "mfLien": 0,
          "mtm": 0,
          "nriPinsBalance": 0,
          "optionPremium": 0,
          "realizedPL": 0,
          "securityMargin": 0,
          "totalMargin": 999999999
        },
        "options": {
          "additionalOptionBrokerage": 0,
          "availableCashBalance": 999999999,
          "clientGroupLimit": 0,
          "debtorFlag": 0,
          "dtv": 0,
          "dtvBTSTSell": 0,
          "initialMargin": 0,
          "marginAvailable": 999999572.4,
          "marginUtilised": 426.6,
          "mfLien": 0,
          "mtm": 0,
          "nriPinsBalance": 0,
          "optionPremium": 0,
          "realizedPL": 0,
          "securityMargin": 0,
          "totalMargin": 999999999
        }
      },
      {
        "exchange": "BSE",
        "futures": {
          "additionalOptionBrokerage": 0,
          "availableCashBalance": 999999999,
          "clientGroupLimit": 0,
          "debtorFlag": 0,
          "dtv": 0,
          "dtvBTSTSell": 0,
          "initialMargin": 0,
          "marginAvailable": 999999572.4,
          "marginUtilised": 426.6,
          "mfLien": 0,
          "mtm": 0,
          "nriPinsBalance": 0,
          "optionPremium": 0,
          "realizedPL": 0,
          "securityMargin": 0,
          "totalMargin": 999999999
        },
        "options": {
          "additionalOptionBrokerage": 0,
          "availableCashBalance": 999999999,
          "clientGroupLimit": 0,
          "debtorFlag": 0,
          "dtv": 0,
          "dtvBTSTSell": 0,
          "initialMargin": 0,
          "marginAvailable": 999999572.4,
          "marginUtilised": 426.6,
          "mfLien": 0,
          "mtm": 0,
          "nriPinsBalance": 0,
          "optionPremium": 0,
          "realizedPL": 0,
          "securityMargin": 0,
          "totalMargin": 999999999
        }
      }
    ],
    "equity": [
      {
        "cash": {
          "additionalOptionBrokerage": 0,
          "availableCashBalance": 999999999,
          "clientGroupLimit": 0,
          "debtorFlag": 0,
          "dtv": 0,
          "dtvBTSTSell": 0,
          "initialMargin": 0,
          "marginAvailable": 999999572.4,
          "marginUtilised": 426.6,
          "mfLien": 0,
          "mtm": 0,
          "nriPinsBalance": 0,
          "optionPremium": 0,
          "realizedPL": 0,
          "securityMargin": 0,
          "totalMargin": 999999999
        },
        "exchange": "NSE,BSE",
        "mis": {
          "misCutOff": 0,
          "misPnl": 0,
          "refreshTime": 15
        },
        "mtf": {
          "additionalOptionBrokerage": 0,
          "availableCashBalance": 999999999,
          "clientGroupLimit": 0,
          "debtorFlag": 0,
          "dtv": 0,
          "dtvBTSTSell": 0,
          "initialMargin": 0,
          "marginAvailable": 999999572.4,
          "marginUtilised": 0,
          "mfLien": 0,
          "mtm": 0,
          "nriPinsBalance": 0,
          "optionPremium": 0,
          "realizedPL": 0,
          "securityMargin": 0,
          "totalMargin": 999999999
        }
      }
    ]
  }
}

```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the Margin details by client for order. |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

