

# PostMetricRow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **String** | The day, with granularity&#x3D;day. |  [optional] |
|**postId** | **String** | The Zernio post, null for a post published outside Zernio. |  |
|**externalPostId** | **String** | The synced post, null while a published post waits for its first sync. |  |
|**accountId** | **String** |  |  |
|**profileId** | **String** |  |  |
|**platform** | **String** |  |  |
|**platformPostId** | **String** |  |  |
|**platformPostUrl** | **String** |  |  |
|**publishedAt** | **String** |  |  |
|**lastSyncedAt** | **String** |  |  |
|**syncStatus** | [**SyncStatusEnum**](#SyncStatusEnum) |  |  |
|**syncError** | [**PostMetricRowSyncError**](PostMetricRowSyncError.md) |  |  |
|**isOwner** | **Boolean** |  |  |
|**isAd** | **Boolean** |  |  |
|**metrics** | **Map&lt;String, BigDecimal&gt;** | Each metric asked; null when the platform does not report it or no snapshot exists yet. |  |
|**breakdowns** | [**Map&lt;String, PostMetricRowBreakdownsValue&gt;**](PostMetricRowBreakdownsValue.md) |  |  [optional] |
|**post** | [**PostMetricContent**](PostMetricContent.md) |  |  [optional] |
|**authenticity** | [**PostMetricAuthenticity**](PostMetricAuthenticity.md) |  |  [optional] |
|**samples** | [**List&lt;PostMetricSample&gt;**](PostMetricSample.md) | With include&#x3D;samples: the readings of the publication, oldest first. |  [optional] |



## Enum: SyncStatusEnum

| Name | Value |
|---- | -----|
| SYNCED | &quot;synced&quot; |
| PENDING | &quot;pending&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



