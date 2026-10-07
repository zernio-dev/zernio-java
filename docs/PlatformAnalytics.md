

# PlatformAnalytics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**platformPostId** | **String** | The native post ID on the platform (e.g. Instagram media ID, tweet ID) |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountUsername** | **String** |  |  [optional] |
|**analytics** | [**PostAnalytics**](PostAnalytics.md) |  |  [optional] |
|**syncStatus** | [**SyncStatusEnum**](#SyncStatusEnum) | Sync state of analytics for this platform |  [optional] |
|**platformPostUrl** | **URI** |  |  [optional] |
|**errorMessage** | **String** | Failure detail. On failed entries, why the post failed to publish. On unavailable entries, why analytics cannot be synced (e.g. Google Business Profile, a TikTok upload that never received a video id). On pending entries, the most recent analytics sync error for the account (null while no sync has failed), cleared after the next successful sync. |  [optional] |
|**errorCode** | [**ErrorCodeEnum**](#ErrorCodeEnum) | Stable machine-readable reason for errorMessage. post_not_found: the post was deleted or is no longer visible to the account. not_post_owner: the post is owned by another Page or user (collab or visitor post); its analytics cannot be read with this Page&#39;s token. permission_missing: the last analytics sync of the Facebook account failed because the Page no longer grants pages_read_engagement (pending entries only). null: no stable code, read errorMessage. New values may be added. |  [optional] |
|**isOwner** | **Boolean** | Facebook only: true when the connected Page authored the post, false when Facebook reports another author (a collab post), null when unknown or for other platforms. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PUBLISHED | &quot;published&quot; |
| FAILED | &quot;failed&quot; |



## Enum: SyncStatusEnum

| Name | Value |
|---- | -----|
| SYNCED | &quot;synced&quot; |
| PENDING | &quot;pending&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



## Enum: ErrorCodeEnum

| Name | Value |
|---- | -----|
| POST_NOT_FOUND | &quot;post_not_found&quot; |
| NOT_POST_OWNER | &quot;not_post_owner&quot; |
| PERMISSION_MISSING | &quot;permission_missing&quot; |



