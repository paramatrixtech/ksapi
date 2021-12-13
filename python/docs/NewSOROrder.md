# NewSOROrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrumentToken** | **int** | Instrument token of the scrip to be traded | [optional] 
**transactionType** | **str** | Transaction Type - BUY or SELL | [optional] 
**quantity** | **int** | Order quantity - specified in same unit as quoted in market depth | [optional] 
**price** | **float** | Order Price for SOR order is always zero i.e. Market Order | [optional] 
**validity** | **str** | Validity of the order - GFD for SOR by default | [optional] 
**variety** | **str** | Variety of the SOR order - REGULAR by Default. | [optional] 
**disclosedQuantity** | **int** | Quantity to be disclosed in order | [optional] 
**triggerPrice** | **float** | Trigger price, required for stoploss or supermultiple order | [optional] 
**tag** | **str** | Tag for this order | [optional] 

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


