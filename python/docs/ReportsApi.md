# ks_api_client.ReportsApi

All URIs are relative to "host" parameter

Method | Description
------------- | -------------
[**order_report**](ReportsApi.md#order_report) | Get order report
[**trade_report**](ReportsApi.md#trade_report)  | Get trade report


# **order_report**
> object order_report(order_id)

Get order report

Returns the full order report for a client in case order_id is not provided 
else returns the order report for a client of provided order_id.

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "", \
                        host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = "")

#First initialize session and generate session token
try:
    # Get full order report
    client.order_report()
	
    # Get order report by order id
    client.order_report(order_id = "2200922000576")

    # Get fno order report by order id
    client.order_report(order_id = "2200922000576", is_fno = "Y")

except Exception as e:
    print("Exception when calling ReportsApi->order_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  Order ID of the order  | [optional]
 **is_fno** | **str** | Is order of FNO type? ("Y" or "N") | [optional]

### Return type

object

### Sample response
```python3
{
  "success": [
    {
      "activityTimestamp": "Aug 25 2021 10:24:04:000AM",
      "disclosedQuantity": 0,
      "exchOrderId": "",
      "exchTradeId": "-",
      "exchangeStatus": "Order sent to Exchange",
      "filledQuantity": 0,
      "message": "",
      "orderQuantity": 1,
      "price": 0,
      "status": "NEWF",
      "statusInfo": "Confirmation Pending",
      "statusMessage": "Confirmation pending from Exchange",
      "triggerPrice": 0,
      "validity": "Good For Day",
      "version": 1
    },
    {
      "activityTimestamp": "Aug 25 2021 10:24:05:000AM",
      "disclosedQuantity": 0,
      "exchOrderId": "1000000000002144",
      "exchTradeId": "-",
      "exchangeStatus": "Order Confirmed",
      "filledQuantity": 0,
      "message": "",
      "orderQuantity": 1,
      "price": 0,
      "status": "OPN",
      "statusInfo": "",
      "statusMessage": "Open",
      "triggerPrice": 0,
      "validity": "Good For Day",
      "version": 2
    }
  ]
}
```

### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order Report of a client |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **trade_report**
> object trade_report(order_id)

Get trade report

Returns the full trade report for a client in case order_id is not provided 
else returns the trade report for a client of provided order_id.

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "", \
                        host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = "")
				
#First initialize session and generate session token

try:
    # Get full trade report
    client.trade_report()
	
    # Get trade report by order id
    client.trade_report(order_id = "2211111002990")

    # Get fno trade report by order id
    client.trade_report(order_id = "2211111002990", is_fno = "Y")
	
except ApiException as e:
    print("Exception when calling ReportsApi->trade_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  Order ID of the order| [optional]
 **is_fno** | **str** | Is order of FNO type? ("Y" or "N") | [optional]

### Return type

object

### Sample response
```python3
{
  'success': [
    {
      'activityTimestamp': 'Dec  8 2021 12: 08: 24: 000PM', 
      'disclosedQuantity': 0, 
      'exchOrderId': '', 
      'exchTradeId': '-', 
      'exchangeStatus': 'Order sent to Exchange', 
      'filledQuantity': 0, 
      'message': '', 
      'orderQuantity': 25, 
      'price': 36157, 
      'status': 'NEWF', 
      'statusInfo': 'Confirmation Pending', 
      'statusMessage': 'Confirmation pending from Exchange', 
      'triggerPrice': 0, 
      'validity': 'Good For Day', 
      'version': 1
    }, 
    {
      'activityTimestamp': 'Dec  8 2021 12: 08: 24: 000PM', 
      'disclosedQuantity': 0, 
      'exchOrderId': '1100000000032549', 
      'exchTradeId': '-', 
      'exchangeStatus': 'Order Confirmed', 
      'filledQuantity': 0, 
      'message': '', 
      'orderQuantity': 25, 
      'price': 36157, 
      'status': 'OPN',
      'statusInfo': '', 
      'statusMessage': 'Open', 
      'triggerPrice': 0, 
      'validity': 'Good For Day', 
      'version': 2
    }
  ]
}
```

### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Trade Report of a client |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
