# ks_api_client.StreamingApi

All URIs are relative to "host" parameter

Method | Description
------------- | ------------- 
[**subscribe**](StreamingApi.md#subscribe) | Get streaming service subscription for specified instruments inputs
[**unsubscribe**](StreamingApi.md#unsubscribe) | Request to unsubscribe from streaming service

# **subscribe**
> object subscribe(input_tokens, callback, broadcast_host):

Get streaming service subscription for specified instruments inputs.

### Example


```python 
from ks_api_client import ks_api 

client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "", \
                        host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = "")

try:
    def callback_method(message):
        print(message)
        print("Your logic/computation will come here.")
    # subscribe to the streamingAPI
    client.subscribe(input_tokens="745,754", callback=callback_method, broadcast_host="https://wstreamer.kotaksecurities.com/feed")
except Exception as e:
    print("Exception when calling StreamingApi->subscribe: %s\n" % e)
```

### Parameters

Name | Type | Description | Notes 
------------- | ------------- | ------------- | ------------- 
**input_tokens** | **str** | Instrument tokens (comma seperated with no spaces). | Example: "475,745" 
**callback** | **obj** | Method object | method of function should have one mandatory parameter to accept message.
**broadcast_host** | **str** | String broadcast host URL | URL for price feed: "https://wstreamer.kotaksecurities.com/feed" (default), and for order status updates: "https://wstreamer.kotaksecurities.com/feed/orders"

### Return type

**object**

### Response Structure

Index | Description
------------- | -------------
0| -
1| -
2| Best buy price
3| Best buy quantity
4| Best sell price
5| Best sell quantity
6| Last trade price
7| High price
8| Low price
9| Average trade price
10| Closing price
11| Open price
12| Net change percentage
13| Total sell quantity
14| Total buy quantity
15| Total trade quantity
16| Open Interest
17| Total trade value
18| Last trade quantity
19| Last trade time
20| Net change
21| Upper circuit limit
22| Lower circuit limit


# **unsubscribe**
> object unsubscribe()

Request to unsubscribe from streaming service.

### Example


```python 
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "", \
                        host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = "")

try:
    # unsubscribe to the streamingAPI
    client.unsubscribe()
except Exception as e: 
    print("Exception when calling StreamingApi->unsubscribe: %s\n" % e)
```

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
