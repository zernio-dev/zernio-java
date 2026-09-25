

# ListAdAccounts200ResponseAccountsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform ad account ID (e.g. act_123) |  [optional] |
|**name** | **String** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**businessId** | **String** | Meta only. Owning Business Manager ID when available on the grant. |  [optional] |
|**businessName** | **String** | Owning business name when supplied by the platform. |  [optional] |
|**status** | **String** | LinkedIn only. LinkedIn&#39;s own ad account status. In practice always &#x60;ACTIVE&#x60;, because the LinkedIn query filters to active accounts. Meta, Google, TikTok and Pinterest report &#x60;accountStatus&#x60; instead; X reports &#x60;approvalStatus&#x60;. |  [optional] |
|**accountStatus** | **Object** |  |  [optional] |
|**approvalStatus** | **String** | X only. X&#39;s own ad account approval status. Observed values are &#x60;ACCEPTED&#x60;, &#x60;PENDING&#x60; and &#x60;REJECTED&#x60;, but X does not publish the full vocabulary, so treat an unrecognised value as not usable. Other platforms report &#x60;accountStatus&#x60; or &#x60;status&#x60; instead. |  [optional] |
|**disableReason** | **Integer** | Meta only. Meta&#39;s &#x60;disable_reason&#x60; code, forwarded unchanged. Present when &#x60;accountStatus&#x60; is &#x60;2&#x60; (DISABLED) and Meta gives a reason, which is what separates a policy action from a payment problem. Meta does not publish a stable list of values for this field, so none are enumerated here: resolve the code against Meta&#39;s own ad account reference. Absent when Meta reports no reason, or when the connected token cannot read the field. |  [optional] |
|**timezoneName** | **String** | IANA timezone of the ad account (Meta only). Drives daily-budget reset and Insights day boundaries. |  [optional] |
|**timezoneOffsetHoursUtc** | **BigDecimal** | Signed UTC offset in hours, reflecting current DST (Meta only). |  [optional] |
|**minimumDailyBudget** | **BigDecimal** | Meta only. Minimum daily budget for the account, in the account currency&#39;s major units. This is the impressions-billed minimum; other billing events have higher minimums. Absent when the connected token cannot read it. |  [optional] |
|**fundingSource** | **String** | Meta only. Meta&#39;s &#x60;funding_source&#x60; ID for the ad account, forwarded unchanged. ABSENT both when this connection&#39;s token cannot see billing and when the account has no payment method; read &#x60;billingStatus&#x60; to tell the two apart. |  [optional] |
|**fundingSourceDetails** | [**ListAdAccounts200ResponseAccountsInnerFundingSourceDetails**](ListAdAccounts200ResponseAccountsInnerFundingSourceDetails.md) |  |  [optional] |
|**billingStatus** | [**BillingStatusEnum**](#BillingStatusEnum) | Meta only. Whether the ad account has a payment method, derived as follows: - &#x60;missing&#x60; when &#x60;accountStatus&#x60; is &#x60;3&#x60; (UNSETTLED) or &#x60;9&#x60; (IN_GRACE_PERIOD),   when &#x60;disableReason&#x60; is &#x60;3&#x60; (RISK_PAYMENT), or when the connected person   has the MANAGE task on the account (admin, who always sees billing) and   Meta returns no funding source. Ad creation on such an account fails at   the ad step with Meta code 100 / subcode 1359188: add a payment method in   Meta&#39;s Billing &amp; payments center. - &#x60;ok&#x60; when Meta returns a funding source. This is presence, not validity:   Meta can still refuse the card or balance at ad creation. - &#x60;unknown&#x60; when the connected person is not an admin of the account, or   the token cannot read the billing fields.  |  [optional] |
|**selectable** | **Boolean** | Meta and X only. Whether the account can create/run ads now. Absent (treat as true) on other platforms. |  [optional] |
|**unusableReason** | **String** | Meta and X only. Human-readable reason when selectable is false; null when selectable. |  [optional] |



## Enum: BillingStatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;ok&quot; |
| MISSING | &quot;missing&quot; |
| UNKNOWN | &quot;unknown&quot; |



