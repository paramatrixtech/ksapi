# ks_api_client.QuoteApi

All URIs are relative to *https://tradeapi.kotaksecurities.com/apim*

Method | Description
------------- | -------------
[**quote**](QuoteApi.md#quote_details) | Get&#39;s Quotes.


# **quote_details**
> object quote(instrument_token, quote_type)

Get Quote Details

Returns full quote details in case quote_type is not provided 
else returns quote details of provided quote_type.

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                 consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

#First initialize session and generate session token

try:
    # Get full quote details
    client.quote(instrument_token = 110)
    
    # Get quote details by quote_type
    client.quote(instrument_token = 110, quote_type = "LTP")
except Exception as e:
    print("Exception when calling QuoteApi->quote_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_token** | **str**|  | 
 **quote_type** | **str** |  Type of Quote details - LTP, DEPTH, OHLC | [optional]

### Return type

object

### Sample response

```python
{
  "success": [
    {
      "wtoken": "110",
      "ltp": "40.4500",
      "lv_net_chg": "0.011000000000000001",
      "lv_net_chg_perc": "0.027954",
      "open_price": "40.0000",
      "closing_price": "39.3500",
      "high_price": "40.4500",
      "low_price": "39.8000",
      "average_trade_price": "40.3900",
      "last_trade_qty": "1472",
      "BD_last_traded_time": "25/08/2021 11:41:20",
      "OI": "0",
      "BD_TTQ": "1658",
      "market_exchange": "BSE",
      "stk_name": "CORALFINAC",
      "display_segment": "EQ",
      "display_fno_eq": ""
    }
  ]
}
```

### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quote fetched successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

