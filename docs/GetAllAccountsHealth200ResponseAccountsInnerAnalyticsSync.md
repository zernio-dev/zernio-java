

# GetAllAccountsHealth200ResponseAccountsInnerAnalyticsSync

Absent on platforms without analytics sync. failing: several consecutive sync attempts failed. stalled: a sync was requested over 6 hours ago and never completed. never_synced: no sync has completed yet. Failing and stalled raise the account status to at least warning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**lastSyncedAt** | **OffsetDateTime** | Last successful sync. Null when never synced or the latest attempt failed. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;ok&quot; |
| FAILING | &quot;failing&quot; |
| STALLED | &quot;stalled&quot; |
| NEVER_SYNCED | &quot;never_synced&quot; |



