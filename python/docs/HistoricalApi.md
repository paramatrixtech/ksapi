# ks_api_client.HistoricalApi

All URIs are relative to *https://tradeapi.kotaksecurities.com/apim*

Method | Description
------------- | -------------
[**history**](HistoricalApi.md#history) | Get historical data


# **get_resource**
> object history(resource, input)

Get historical data based on given resource

Get Historical data

### Example

```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                 consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

#First initialize session and generate session token

try:
    # Get historical prices
    client.history("historicalprices",{"exchange":"bse","cocode":"476","fromdate":"01-jan-2014","todate":"08-oct-2015"})
except Exception as e:
    print("Exception when calling Historical API->details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | Type of resource historicalprices,historicalprices-unadjusted,NSEFNO_HistoricalContinuousChart,LiveorEODHistorical
 **input** | **str**|  | Json as per resource selected

### Return type

**object**


### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Historical Details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

