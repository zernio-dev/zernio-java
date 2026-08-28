

# UsageMeteringAttribution

Present with `groupBy`. The window's spend split per profile or account; `sum(groups) + unattributed` equals `totals` per product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupBy** | [**GroupByEnum**](#GroupByEnum) |  |  [optional] |
|**groups** | [**List&lt;UsageAttributionGroup&gt;**](UsageAttributionGroup.md) |  |  [optional] |
|**unattributed** | [**UsageAttributionSlice**](UsageAttributionSlice.md) | Spend no profile/account can claim: credits, 10DLC fees, Verify, and usage whose record no longer resolves to an account. Zero for a restricted principal. |  [optional] |
|**totals** | [**UsageAttributionSlice**](UsageAttributionSlice.md) | The window totals; for a restricted principal, the sum of the visible groups. |  [optional] |
|**restricted** | **Boolean** | True when the caller (profile-scoped API key or member) cannot see every profile: &#x60;groups&#x60; are filtered, &#x60;totals&#x60; sum them, &#x60;unattributed&#x60; is zero, and the top-level &#x60;days&#x60; / &#x60;totals&#x60; / &#x60;lineItems&#x60; are projected onto the visible groups with &#x60;peaks&#x60;, &#x60;callUsage&#x60; and &#x60;tax&#x60; null. |  [optional] |



## Enum: GroupByEnum

| Name | Value |
|---- | -----|
| PROFILE | &quot;profile&quot; |
| ACCOUNT | &quot;account&quot; |



