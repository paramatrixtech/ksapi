# ks_api_client.TokenApi

All URIs are relative to *https://tradeapi.kotaksecurities.com/apim/oauth/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revoke_post**](DefaultApi.md#revoke_post) | **POST** /revoke | 
[**token_post**](DefaultApi.md#token_post) | **POST** /token | 


# **revoke**
> revoke(token=token, token_type_hint=token_type_hint)



### Example
```python
from ks_api_client import ks_api

# Configure OAuth2 access token for authorization: default
client = ks_api.KSTradeApi(access_token = "", userid = "", consumer_key = "",ip = "127.0.0.1", app_id = "", \
                        hosts=["https://tradeapi.kotaksecurities.com/apim"], proxy_url = '', proxy_user = '', \ 
                        proxy_pass = '', consumer_secret = "consumer_secret")

#First initialize session and generate session token

try:
    client.revoke(token="token", token_type_hint="token_type_hint")
except ApiException as e:
    print("Exception when calling TokenApi->revoke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Base64(consumer-key:consumer-secret) | 
 **token** | **str**| access token you want to revoke | [optional] 
 **token_type_hint** | **str**| (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token**
> token(grant_type=grant_type, username=username, password=password, refresh_token=refresh_token)



### Example
```python
from ks_api_client import ks_api

# Configure OAuth2 access token for authorization: default
client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                 consumer_key = "consumer_key", ip = "IP", app_id = "app_id", consumer_secret = "consumer_secret")

#First initialize session and generate session token

try:
    client.token(grant_type="grant_type", username="username", password="password", refresh_token="refresh_token")
except ApiException as e:
    print("Exception when calling TokenApi->token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Base64(consumer-key:consumer-secret) | 
 **grant_type** | **str**|  | [optional] 
 **username** | **str**| only if grant_type&#x3D;password | [optional] 
 **password** | **str**| only if grant_type&#x3D;password | [optional] 
 **refresh_token** | **str**| only if grant_type&#x3D;refresh_token | [optional] 

### Return type

void (empty response body)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

