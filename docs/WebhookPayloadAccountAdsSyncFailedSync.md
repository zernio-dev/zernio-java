

# WebhookPayloadAccountAdsSyncFailedSync


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastSuccessfulSyncAt** | **OffsetDateTime** |  |  |
|**failureCount** | **Integer** | Consecutive failed sync attempts on the ad account&#39;s ads. |  |
|**errorCategory** | [**ErrorCategoryEnum**](#ErrorCategoryEnum) | ad_account_not_listed &#x3D; the platform no longer returns the ad account to this connection (access removed, or a platform-side change); sync_error &#x3D; the platform returned an error, see &#x60;error&#x60;; stale &#x3D; no sync succeeded and no error was recorded. New values may be added.  |  |
|**error** | **String** | Human-readable detail, for display and debugging. Branch on errorCategory. |  |



## Enum: ErrorCategoryEnum

| Name | Value |
|---- | -----|
| AD_ACCOUNT_NOT_LISTED | &quot;ad_account_not_listed&quot; |
| SYNC_ERROR | &quot;sync_error&quot; |
| STALE | &quot;stale&quot; |



