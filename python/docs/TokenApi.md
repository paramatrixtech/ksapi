# openapi_client.DefaultApi

All URIs are relative to *https://tradeapi.kotaksecurities.com/apim/oauth/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revoke_post**](DefaultApi.md#revoke_post) | **POST** /revoke | 
[**token_post**](DefaultApi.md#token_post) | **POST** /token | 


# **revoke_post**
> revoke_post(authorization, token=token, token_type_hint=token_type_hint)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.DefaultApi(openapi_client.ApiClient(configuration))
authorization = 'authorization_example' # str | Basic Base64(consumer-key:consumer-secret)
token = 'token_example' # str | access token you want to revoke (optional)
token_type_hint = 'token_type_hint_example' # str | (optional) (optional)

try:
    api_instance.revoke_post(authorization, token=token, token_type_hint=token_type_hint)
except ApiException as e:
    print("Exception when calling DefaultApi->revoke_post: %s\n" % e)
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

# **token_post**
> token_post(authorization, grant_type=grant_type, username=username, password=password, refresh_token=refresh_token)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
configuration = openapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openapi_client.DefaultApi(openapi_client.ApiClient(configuration))
authorization = 'authorization_example' # str | Basic Base64(consumer-key:consumer-secret)
grant_type = 'grant_type_example' # str |  (optional)
username = 'username_example' # str | only if grant_type=password (optional)
password = 'password_example' # str | only if grant_type=password (optional)
refresh_token = 'refresh_token_example' # str | only if grant_type=refresh_token (optional)

try:
    api_instance.token_post(authorization, grant_type=grant_type, username=username, password=password, refresh_token=refresh_token)
except ApiException as e:
    print("Exception when calling DefaultApi->token_post: %s\n" % e)
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

