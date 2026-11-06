

# AutomationStepOneOf7

Changes a Google campaign's target CPA or target ROAS by a percent, bounded like a budget change.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**target** | [**TargetEnum**](#TargetEnum) |  |  |
|**by** | **String** |  |  |
|**max** | **BigDecimal** |  |  [optional] |
|**min** | **BigDecimal** |  |  [optional] |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| TARGET | &quot;target&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADS_CHANGE_TARGET | &quot;ads.change_target&quot; |



## Enum: TargetEnum

| Name | Value |
|---- | -----|
| CPA | &quot;cpa&quot; |
| ROAS | &quot;roas&quot; |



