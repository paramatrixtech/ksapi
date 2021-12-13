# NewMTFOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrumentToken** | **int** | Instrument token of the scrip to be traded | [optional] 
**transactionType** | **str** | Transaction Type - BUY or SELL | [optional] 
**quantity** | **int** | Order quantity - specified in same unit as quoted in market depth | [optional] 
**price** | **float** | Order Price, non zero positive for limit order and zero for market order | [optional] 
**validity** | **str** | Validity of the order - GFD, IOC etc | [optional] 
**variety** | **str** | Variety of the order - REGULAR, AMO, SQUAREOFF - for Super Multiple Orders etc | [optional] 
**disclosedQuantity** | **int** | Quantity to be disclosed in order | [optional] 
**triggerPrice** | **float** | Trigger price, required for stoploss or supermultiple order | [optional] 
**tag** | **str** | Tag for this order | [optional] 

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


