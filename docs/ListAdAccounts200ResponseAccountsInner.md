

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
|**selectable** | **Boolean** | Meta only. Whether the account can create/run ads now. Absent (treat as true) on non-Meta platforms. |  [optional] |
|**unusableReason** | **String** | Meta only. Human-readable reason when selectable is false; null when selectable. |  [optional] |



