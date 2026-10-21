

# GetAdAccountBilling200ResponseAccountBudgetsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountBudgetId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**billingSetupId** | **String** |  |  [optional] |
|**approvedSpendingLimitMicros** | **String** |  |  [optional] |
|**approvedSpendingLimitType** | **String** | INFINITE for an unlimited budget. |  [optional] |
|**pendingProposalId** | **String** | Account budget proposal still waiting for Google&#39;s review. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| APPROVED | &quot;APPROVED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



