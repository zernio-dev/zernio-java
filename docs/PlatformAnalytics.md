

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
|**errorMessage** | **String** | Error details when status is failed, or why analytics are unavailable for a published entry (e.g. Google Business Profile, a TikTok upload that never received a video id) |  [optional] |



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



