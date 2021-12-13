# ExistingOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orderId** | **str** | Order ID of the order to be modified | 
**quantity** | **int** | Order quantity - specified in same unit as quoted in market depth | [optional] 
**price** | **float** | Order Price, non zero positive for limit order and zero for market order | [optional] 
**disclosedQuantity** | **int** | Quantity to be disclosed in order | [optional] 
**triggerPrice** | **float** | Trigger price, required for stoploss or supermultiple order | [optional] 
**validity** | **str** | Validity of the order - GFD, IOC etc | [optional] 
**tslo** | [**Tslomodify**](Tslomodify.md) |  | [optional] 
**bracket** | [**Bracketmodify**](Bracketmodify.md) |  | [optional] 
**tslonew** | [**Tslomodify**](Tslomodify.md) |  | [optional] 
**bracketnew** | [**Bracketmodify**](Bracketmodify.md) |  | [optional] 
**gtc** | [**Gtcmodify**](Gtcmodify.md) |  | [optional] 
**ctd** | [**Ctdmodify**](Ctdmodify.md) |  | [optional] 
**cod** | [**Codmodify**](Codmodify.md) |  | [optional] 

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


