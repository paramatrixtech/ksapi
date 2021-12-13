# NewOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrumentToken** | **int** | Instrument token of the scrip to be traded | [optional] 
**transactionType** | **str** | Transaction Type - BUY or SELL | [optional] 
**quantity** | **int** | Order quantity - specified in same unit as quoted in market depth | [optional] 
**price** | **float** | Order Price, non zero positive for limit order and zero for market order | [optional] 
**product** | **str** | Product type for this order - NORMAL, SUPERMULTIPLE, SUPERMULTIPLEOPTION, MTF | [optional] 
**validity** | **str** | Validity of the order - GFD, IOC etc | [optional] 
**variety** | **str** | Variety of the order - REGULAR, AMO, SQUAREOFF - for Super Multiple Orders etc | [optional] 
**disclosedQuantity** | **int** | Quantity to be disclosed in order | [optional] 
**triggerPrice** | **float** | Trigger price, required for stoploss or supermultiple order | [optional] 
**tslo** | [**Tsloplace**](Tsloplace.md) |  | [optional] 
**bracket** | [**Bracketplace**](Bracketplace.md) |  | [optional] 
**tslonew** | [**Tsloplace**](Tsloplace.md) |  | [optional] 
**bracketnew** | [**Bracketplace**](Bracketplace.md) |  | [optional] 
**gtc** | [**Gtcplace**](Gtcplace.md) |  | [optional] 
**ctd** | [**Ctdplace**](Ctdplace.md) |  | [optional] 
**cod** | [**Codplace**](Codplace.md) |  | [optional] 
**tag** | **str** | Tag for this order | [optional] 
**smartOrderRouting** | **str** | smart Order Routing for this order | [optional] 

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


