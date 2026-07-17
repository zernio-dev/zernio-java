

# ListAdAccounts200ResponseAccountsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform ad account ID (e.g. act_123) |  [optional] |
|**name** | **String** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**timezoneName** | **String** | IANA timezone of the ad account (Meta only). Drives daily-budget reset and Insights day boundaries. |  [optional] |
|**timezoneOffsetHoursUtc** | **BigDecimal** | Signed UTC offset in hours, reflecting current DST (Meta only). |  [optional] |
|**minimumDailyBudget** | **BigDecimal** | Meta only. Minimum daily budget for the account, in the account currency&#39;s major units. This is the impressions-billed minimum; other billing events have higher minimums. Absent when the connected token cannot read it. |  [optional] |
|**selectable** | **Boolean** | Meta and X only. Whether the account can create/run ads now. Absent (treat as true) on other platforms. |  [optional] |
|**unusableReason** | **String** | Meta and X only. Human-readable reason when selectable is false; null when selectable. |  [optional] |



