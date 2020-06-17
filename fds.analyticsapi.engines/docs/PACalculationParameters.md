# PACalculationParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**componentid** | **str** | The PA Engine component identifier to analyze. | 
**accounts** | [**list[PAIdentifier]**](PAIdentifier.md) | List of accounts. | [optional] 
**benchmarks** | [**list[PAIdentifier]**](PAIdentifier.md) | List of benchmarks. | [optional] 
**dates** | [**PADateParameters**](PADateParameters.md) |  | [optional] 
**groups** | [**list[PACalculationGroup]**](PACalculationGroup.md) | List of groupings for the PA calculation. This will take precedence over the groupings saved in the PA document. | [optional] 
**currencyisocode** | **str** | Currency ISO code for calculation. | [optional] 
**columns** | [**list[PACalculationColumn]**](PACalculationColumn.md) | List of columns for the PA calculation. This will take precedence over the columns saved in the PA document. | [optional] 
**componentdetail** | **str** | Component detail type for the PA component. It can be GROUPS or TOTALS. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


