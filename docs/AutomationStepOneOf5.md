

# AutomationStepOneOf5

Changes a Meta ad set's bid cap or cost cap by a percent, bounded like a budget change. An ad set without one is skipped.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**by** | **String** | Up to +100% or down to -90%. |  |
|**max** | **BigDecimal** |  |  [optional] |
|**min** | **BigDecimal** |  |  [optional] |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| BID | &quot;bid&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADS_CHANGE_BID | &quot;ads.change_bid&quot; |



