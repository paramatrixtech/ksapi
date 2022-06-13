# ks_api_client.OrderApi

All URIs are relative to "host" parameter

Method | Description | Response Normal Order | Response SOR Order | Response MTF Order |
------------- | ------------- | -------------- | ---------------- | --------------- |
[**place_order**](OrderApi.md#place_new_order) | Place a New order | {'Success': {'NSE': {'message': 'Your Order has been Placed and Forwarded to the Exchange: XXXXXXXXXXXX.', 'orderId': XXXXXXXXXXXXXX, 'price': 0, 'quantity': 1, 'tag': ''}}} | {'Success': {'BSE': {'message': '', 'orderId': 0, 'price': 0, 'quantity': 0, 'tag': ''}, 'NSE': {'message': '**Smart Order1,Message: Placed 1 Qty in NSE,Abws Order Number XXXXXXXXXX\|1T028\|NN\|1\|0.000000', 'orderId': 2210806000026, 'price': 0, 'quantity': 1, 'tag': ''}}} | {'Success': {'NSE': {'message': 'Your Order has been Placed and Forwarded to the Exchange: XXXXXXXXXX.', 'orderId': XXXXXXXXX, 'price': 0, 'quantity': 1, 'tag': ''}}}
[**modify_order**](OrderApi.md#modify_order) | Modify an existing order |
[**cancel_order**](OrderApi.md#cancel_order) | Cancel an order |

# **place_new_order**
> object place_order(order_type, instrument_token, transaction_type, quantity, price, disclosed_quantity , trigger_price, tag , validity , variety , product , smart_order_routing)

Place a New order

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "", \
                        host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = "")

#First initialize session and generate session token

try:
    # Place a Order
    client.place_order(order_type = "N", instrument_token = 727, transaction_type = "BUY", quantity = 1, price = 0, \
                   disclosed_quantity = 0, trigger_price = 0, tag = "string", validity = "GFD", variety = "REGULAR" \ 
                   product = "NORMAL" ,smart_order_routing="string")
except Exception as e:
    print("Exception when calling OrderApi->place_order: %s\n" % e)
``` 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**order_type** | **str**| Type of the order - N(NormalOrder), SOR(Smart Order Routing Order), MTF(Margin Trading Facility Order), MIS(Margin Intraday Sqaure-Off)|
**instrument_token** | **int** | Instrument token of the scrip to be traded.<br> Instrument tokens can be found at the following urls (NOTE: Please replace DD_MM_YYYY with the latest date for updated instrument tokens, for example 27_05_2021 will give tokens for 27 may):<br> Equity: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_DD_MM_YYYY.txt <br> Derivatives: https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_DD_MM_YYYY.txt |
**transaction_type** | **str** | Transaction Type - BUY or SELL |
**quantity** | **int** | Order quantity - specified in same unit as quoted in market depth |
**price** | **float** | Order Price, non zero positive for limit order and zero for market order |
**disclosed_quantity** | **int** | Quantity to be disclosed in order | [optional] 
**trigger_price** | **float** | Trigger price, required for stoploss or supermultiple order | [optional] 
**validity** | **str** | Validity of the order - GFD, IOC etc | [optional] 
**variety** | **str** | Variety of the order - REGULAR, AMO, SQUAREOFF - for Super Multiple Orders etc | [optional] 
**tag** | **str** | Tag for this order | [optional] 
**product** | **str** | Product type for this order - NORMAL, SUPERMULTIPLE, SUPERMULTIPLEOPTION, MTF | [optional]
**smart_order_routing** | **str** | smart Order Routing for this order | [optional]

### Return type

**object**

### Sample response

```python
{
  "Success": {
    "NSE": {
      "message": "Your Order has been Placed and Forwarded to the Exchange: 2210823000018.",
      "orderId": 2210823000018,
      "price": 1801,
      "quantity": 1,
      "tag": "string"
    }
  }
}
```
### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order placed successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)

# **modify_order**
> object modify_order(order_id, price , quantity , disclosed_quantity, trigger_price)

Modify an existing order

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "", \
                        host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = "")

#First initialize session and generate session token

try:
    # Modify an existing order
    client.modify_order(order_id = "2200922000576", price = 0, quantity = 1, \
                 disclosed_quantity = 0, trigger_price = 0, validity = "GFD")
								  
except Exception as e:
    print("Exception when calling OrderApi->modify_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**order_id** | **str** | Order ID of the order to be modified | 
**quantity** | **int** | Order quantity - specified in same unit as quoted in market depth |
**price** | **float** | Order Price, non zero positive for limit order and zero for market order | 
**disclosed_quantity** | **int** | Quantity to be disclosed in order | 
**trigger_price** | **float** | Trigger price, required for stoploss or supermultiple order |
**validity** | **str** | Validity of the order - GFD, IOC etc | [optional]

### Return type

**object**

### Sample response

```python
{
  "Success": {
    "NSE": {
      "message": "Your Order has been Modified Successfully for Order No : 2210825000008",
      "orderId": 2210825000008,
      "price": 1804,
      "quantity": 1,
      "tag": ""
    }
  }
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order modified successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)


# **cancel_order**
> object cancel_order(order_id)

Cancel an order

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "", \
                        host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = "")

#First initialize session and generate session token

try:
    # Cancel an order
    client.cancel_order(order_id = "2200922000576")
except Exception as e:
    print("Exception when calling OrderApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID to cancel. | 

### Return type

**object**

### Sample response

```python
{
  "Success": {
    "NSE": {
      "message": "Your Order for ACC EQ NSE has been Cancelled Successfully for Order No : 2210825000008",
      "orderId": 2210825000008,
      "price": 0,
      "quantity": 0,
      "tag": ""
    }
  }
}
```

### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order cancelled successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)


