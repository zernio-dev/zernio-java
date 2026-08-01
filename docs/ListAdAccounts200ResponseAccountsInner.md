

# ListAdAccounts200ResponseAccountsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform ad account ID (e.g. act_123) |  [optional] |
|**name** | **String** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**status** | **String** | LinkedIn only. LinkedIn&#39;s own ad account status. In practice always &#x60;ACTIVE&#x60;, because the LinkedIn query filters to active accounts. Meta, Google, TikTok and Pinterest report &#x60;accountStatus&#x60; instead; X reports &#x60;approvalStatus&#x60;. |  [optional] |
|**accountStatus** | **Object** |  |  [optional] |
|**approvalStatus** | **String** | X only. X&#39;s own ad account approval status. Observed values are &#x60;ACCEPTED&#x60;, &#x60;PENDING&#x60; and &#x60;REJECTED&#x60;, but X does not publish the full vocabulary, so treat an unrecognised value as not usable. Other platforms report &#x60;accountStatus&#x60; or &#x60;status&#x60; instead. |  [optional] |
|**disableReason** | **Integer** | Meta only. Meta&#39;s &#x60;disable_reason&#x60; code, forwarded unchanged. Present when &#x60;accountStatus&#x60; is &#x60;2&#x60; (DISABLED) and Meta gives a reason, which is what separates a policy action from a payment problem. Meta does not publish a stable list of values for this field, so none are enumerated here: resolve the code against Meta&#39;s own ad account reference. Absent when Meta reports no reason, or when the connected token cannot read the field. |  [optional] |
|**timezoneName** | **String** | IANA timezone of the ad account (Meta only). Drives daily-budget reset and Insights day boundaries. |  [optional] |
|**timezoneOffsetHoursUtc** | **BigDecimal** | Signed UTC offset in hours, reflecting current DST (Meta only). |  [optional] |
|**minimumDailyBudget** | **BigDecimal** | Meta only. Minimum daily budget for the account, in the account currency&#39;s major units. This is the impressions-billed minimum; other billing events have higher minimums. Absent when the connected token cannot read it. |  [optional] |
|**selectable** | **Boolean** | Meta and X only. Whether the account can create/run ads now. Absent (treat as true) on other platforms. |  [optional] |
|**unusableReason** | **String** | Meta and X only. Human-readable reason when selectable is false; null when selectable. |  [optional] |



