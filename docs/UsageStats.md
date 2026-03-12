

# UsageStats


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**planName** | **String** |  |  [optional] |
|**billingPeriod** | [**BillingPeriodEnum**](#BillingPeriodEnum) |  |  [optional] |
|**signupDate** | **OffsetDateTime** |  |  [optional] |
|**billingAnchorDay** | **Integer** | Day of month (1-31) when the billing cycle resets |  [optional] |
|**limits** | [**UsageStatsLimits**](UsageStatsLimits.md) |  |  [optional] |
|**usage** | [**UsageStatsUsage**](UsageStatsUsage.md) |  |  [optional] |



## Enum: BillingPeriodEnum

| Name | Value |
|---- | -----|
| MONTHLY | &quot;monthly&quot; |
| YEARLY | &quot;yearly&quot; |



