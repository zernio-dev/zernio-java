

# AutomationStepOneOf8

Sets a Google campaign's target CPA (ad account currency) or target ROAS (a ratio, 3 is 300%).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**target** | [**TargetEnum**](#TargetEnum) |  |  |
|**amount** | **BigDecimal** |  |  |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| TARGET | &quot;target&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADS_SET_TARGET | &quot;ads.set_target&quot; |



## Enum: TargetEnum

| Name | Value |
|---- | -----|
| CPA | &quot;cpa&quot; |
| ROAS | &quot;roas&quot; |



