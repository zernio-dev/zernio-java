

# AdCampaignBudget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**amountMicros** | **String** | Google only. Exact decimal micros; DAILY uses amount_micros and CUSTOM_PERIOD uses total_amount_micros. |  [optional] |
|**explicitlyShared** | **Boolean** | Google only. True for a shared budget; null when unavailable. Shared writes require allowSharedBudgetUpdate&#x3D;true; unknown sharing status cannot be overridden. |  [optional] |
|**resourceName** | **String** | Google only. campaign_budget.resource_name, or null when unavailable. |  [optional] |
|**deliveryMethod** | **String** | Google only. campaign_budget.delivery_method, typically STANDARD, or null when unavailable. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| LIFETIME | &quot;lifetime&quot; |



