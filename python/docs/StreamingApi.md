# ks_api_client.StreamingApi

All URIs are relative to *https://tradeapi.kotaksecurities.com/apim*

Method | Description ------------- | ------------- 
[**subscribe**](StreamingApi.md#subscribe) | Get Margin Required for an order by amount or quantity.
[**unsubscribe**](StreamingApi.md#unsubscribe) | Gives complete Margin Details of a Client from RMS.

# **subscribe**
> object subscribe(input_tokens, auth_token, callback, broadcast_host):

Get streaming service subscription for specified instruments inputs.

### Example


```python 
from ks_api_client import ks_api 

client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "", \
                        hosts=["https://tradeapi.kotaksecurities.com/apim"], proxy_url = '', proxy_user = '', \ 
                        proxy_pass = '', consumer_secret = "")

#First initialize session and generate session token

try:
    # Get Margin Required for an order by amount or quantity.
    client.subscribe(input_tokens="", consumer_key="", consumer_secret="", callback=print, broadcast_host="https://wstreamer.kotaksecurities.com")
except Exception as e:
    print("Exception when calling StreamingApi->subscribe: %s\n" % e)
```

### Parameters

Name | Type | Description | Notes 
------------- | ------------- | ------------- | ------------- 
**input_tokens** | **str** | Instrument tokens with comma seperated. | Example: "475,745" 
**consumer_key** | **str** | Consumer Key | Mandatory field 
**consumer_secret** | **str** | Consumer Secret | Mandatory field 
**callback** | **obj** | Method object | method of function should have one mandatory parameter to accept message. Default method is print() 
**broadcast_host** | **str** | String host URL | default value: "https://wstreamer.kotaksecurities.com/feed"

### Return type

**object**


# **unsubscribe**
> object unsubscribe()

Request to unsubscribe from streaming service.

### Example


```python 
from ks_api_client import ks_api 
client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \ 
                consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

#First initialize session and generate session token

try:
    # Get Margin details.
    client.unsubscribe() 
except Exception as e: 
    print("Exception when calling StreamingApi->unsubscribe: %s\n" % e)
```

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
