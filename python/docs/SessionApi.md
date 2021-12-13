# ks_api_client.SessionApi

All URIs are relative to *https://tradeapi.kotaksecurities.com/apim*

Method | Description
------------- | -------------
[**ks_api.KSTradeApi**](SessionApi.md#session_init) | Initialise Session
[**login**](SessionApi.md#login) | Login using Userid
[**session_2fa**](SessionApi.md#session_2fa) | Generate final Session Token
[**logout**](SessionApi.md#logout) | Invalidate Session Token


# **session_init**
> ks_api.KSTradeApi(access_token, userid, consumer_key, ip, app_id, host, proxy_url, proxy_user, proxy_pass )

Initialise Session

API to initiate trading session for a User.

### Example


```python
from ks_api_client import ks_api

#the session initializes when following constructor is called
client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **userid** | **str**|  |
 **consumer_key** | **str**|  |
 **ip** | **str**|  |
 **app_id** | **str**|  |
 **host** | **list**| List of trade API host URLs | [optional]
 **proxy_url** | **str**| Proxy url  |  [optional]
 **proxy_user** | **str**| Proxy user's Username | [optional]
 **proxy_pass** | **str**| Proxy user's Password | [optional]
  



### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**400** | Invalid or missing input parameters |  -  |
**401** | Verify resource and path of the request |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **login**
> object login(password)

Login using Userid

Authenticate userid and password to generate one time token.

### Example


```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

try:
    # Login using password
    client.login(password = "password")
except Exception as e:
    print("Exception when calling SessionApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**|  |

### Return type

object

### Sample response
```python
{
    'Success': 
    {   
        'Status': 'Temporary', 
        'accessCodeTime': '8/30/2021 12:01:00 AM',
        'biometric': 'N', 
        'clientType': 'ONLINE',
        'emailId': 'XXXXXXXXXXXXX@kotak.com',
        'message': 'Authentication Successful.',
        'mpin': 'N', 
        'oneTimeToken': 'BE45003A04F44B57926EF852978BC53A', 
        'phoneNo': 'XXXXXXX828', 
        'redirect': 
            {
                'host': 'https://sbx.kotaksecurities.com/apim', 
                'port': 443,
                'userid': 'S4MPL3'
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
**200** | User session validated successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**401** | Verify resource and path of the request |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# **session_2fa**
> object session_2fa(access_code)

Generate final Session Token

API to generate final session for user based on one time token.

### Example


```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")
				
try:
    # Login using password
    client.login(password = "password")
    
    # Generate final Session Token
    client.session_2fa(access_code = "access_code")
except Exception as e:
    print("Exception when calling SessionApi->session_2fa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_code** | **str**|  | [optional]

### Return type

object

### Sample response

```python
{
  "advancedChart": {
    "host": "https://kotaksecurities.com/chartiqtrade/",
    "port": 443
  },
  "apiToken": {
    "redirect": {
      "host": "https://uattradeapi.kotaksecurities.com",
      "port": 443
    },
    "sessionId": "868457#0-2044"
  },
  "broadcast": {
    "host": "https://dtstream.kotaksecurities.com/",
    "port": 443
  },
  "clientCode": "S4ML3",
  "clientName": "KOTAK",
  "dormantType": "-",
  "emailId": "",
  "enabledExchangeSegments": {
    "CASH": [
      {
        "exchange": "NSE",
        "status": "ACTIVE"
      },
      {
        "exchange": "BSE",
        "status": "ACTIVE"
      }
    ],
    "CDS": [
      {
        "exchange": "NSE",
        "status": "ACTIVE"
      },
      {
        "exchange": "MCX",
        "status": "ACTIVE"
      }
    ],
    "COMMODITY": [
      {
        "exchange": "MCX",
        "status": "INACTIVE"
      }
    ],
    "FNO": [
      {
        "exchange": "NSE",
        "status": "ACTIVE"
      },
      {
        "exchange": "BSE",
        "status": "ACTIVE"
      }
    ]
  },
  "enabledProducts": [
    "NORMAL",
    "SUPERMULTIPLE",
    "SUPERMULTIPLEOPTION",
    "MTF",
    "MIS"
  ],
  "enabledSegments": [
    "CASH",
    "FO",
    "CDS"
  ],
  "getLtp": {
    "host": "https://mksapi.kotaksecurities.com",
    "port": 443
  },
  "isNRI": "N",
  "loginTime": "8/23/2021 11:29:35 AM",
  "marginProduct": {
    "isEnabled": "Y"
  },
  "marketData": {
    "host": "https://mksapi.kotaksecurities.com",
    "port": 443
  },
  "phoneNo": "",
  "redirect": {
    "host": "https://sbx.kotaksecurities.com/apim",
    "port": 443
  },
  "search": {
    "host": "https://mksapi.kotaksecurities.com/",
    "port": 443
  },
  "service": {
    "host": "https://sbx.kotaksecurities.com/apim",
    "port": 443
  },
  "sessionToken": "BC604B4A88FF4722844ED8FC3D395DAE",
  "stwtFlag": "Y",
  "userId": "1T040",
  "weblink": {
    "host": "https://mtrade.kotaksecurities.com/",
    "port": 443
  }
}
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User session validated successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**401** | Verify resource and path of the request |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **logout**
> object logout()

Invalidate Session Token

API to invalidate final session for user.

### Example


```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

#First initialize session and generate session token

try:
    # Invalidate Session Tsoken
    client.logout()
except Exception as e:
    print("Exception when calling SessionApi->logout: %s\n" % e)
```


### Return type

object

### Sample respose

```python
{
  "Success": {
    "message": "Logout Successful."
  }
}

```

### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User session invalidated  successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
