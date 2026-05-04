

# UsageStats

Plan and usage stats. The response shape depends on `billingSystem`:   * Stripe users (default): per-period counters like `usage.uploads` and     `usage.profiles` are returned, scoped by the plan's `limits`.   * Metronome users (usage-based): `limits` are unlimited (-1). The     `usage` block carries connected-account and per-X-operation counts,     and the `spend` block carries current-period costs plus the X cap. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingSystem** | [**BillingSystemEnum**](#BillingSystemEnum) | Which billing system the account is on. Shape of &#x60;usage&#x60;/&#x60;spend&#x60; differs. |  [optional] |
|**planName** | **String** |  |  [optional] |
|**billingPeriod** | [**BillingPeriodEnum**](#BillingPeriodEnum) |  |  [optional] |
|**signupDate** | **OffsetDateTime** |  |  [optional] |
|**billingAnchorDay** | **Integer** | Day of month (1-31) when the billing cycle resets |  [optional] |
|**hasAccess** | **Boolean** | True if the account is in good standing. False for past-due/unpaid/paused subscriptions. |  [optional] |
|**customerId** | **String** | Stripe customer ID, when present. |  [optional] |
|**isInvitedUser** | **Boolean** | True if this is a team member; limits/usage reflect the account owner. |  [optional] |
|**autoUpgradeEnabled** | **Boolean** | Stripe-only. Always false for Metronome users. |  [optional] |
|**limits** | [**UsageStatsLimits**](UsageStatsLimits.md) |  |  [optional] |
|**usage** | [**UsageStatsUsage**](UsageStatsUsage.md) |  |  [optional] |
|**spend** | [**UsageStatsSpend**](UsageStatsSpend.md) |  |  [optional] |



## Enum: BillingSystemEnum

| Name | Value |
|---- | -----|
| STRIPE | &quot;stripe&quot; |
| METRONOME | &quot;metronome&quot; |



## Enum: BillingPeriodEnum

| Name | Value |
|---- | -----|
| MONTHLY | &quot;monthly&quot; |
| YEARLY | &quot;yearly&quot; |



