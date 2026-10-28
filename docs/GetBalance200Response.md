

# GetBalance200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableCents** | **Integer** | Balance you can transfer now. Negative after a dispute or refund of a top-up that was already spent; transfers are refused while it is negative. |  [optional] |
|**pendingCents** | **Integer** | Paid card top-ups still on hold. Card top-ups become available after 7 days. |  [optional] |
|**pendingReleases** | [**List&lt;GetBalance200ResponsePendingReleasesInner&gt;**](GetBalance200ResponsePendingReleasesInner.md) | Card top-ups on hold, each with the time it becomes available. |  [optional] |
|**pendingTopupCents** | **Integer** | Top-ups started but not paid yet. |  [optional] |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) |  |  [optional] |
|**recentTopups** | [**List&lt;TreasuryTopup&gt;**](TreasuryTopup.md) |  |  [optional] |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| USD | &quot;usd&quot; |



