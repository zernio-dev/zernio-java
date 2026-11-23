

# GetBroadcast200ResponseBroadcast


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**message** | [**GetBroadcast200ResponseBroadcastMessage**](GetBroadcast200ResponseBroadcastMessage.md) |  |  [optional] |
|**template** | [**GetBroadcast200ResponseBroadcastTemplate**](GetBroadcast200ResponseBroadcastTemplate.md) |  |  [optional] |
|**segmentFilters** | [**GetBroadcast200ResponseBroadcastSegmentFilters**](GetBroadcast200ResponseBroadcastSegmentFilters.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**scheduledAt** | **OffsetDateTime** |  |  [optional] |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**completedAt** | **OffsetDateTime** |  |  [optional] |
|**recipientCount** | **Integer** |  |  [optional] |
|**sentCount** | **Integer** | Recipients whose latest status is &#x60;sent&#x60;: the platform accepted the message and has not confirmed delivery yet. Each recipient counts once, under its latest status, so everyone the broadcast went out to is sentCount + deliveredCount + readCount. |  [optional] |
|**deliveredCount** | **Integer** | Recipients whose latest status is &#x60;delivered&#x60;, not read yet. Everyone it was delivered to is deliveredCount + readCount. |  [optional] |
|**readCount** | **Integer** | Recipients whose latest status is &#x60;read&#x60;. |  [optional] |
|**failedCount** | **Integer** | Recipients whose send failed. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| SENDING | &quot;sending&quot; |
| COMPLETED | &quot;completed&quot; |
| FAILED | &quot;failed&quot; |
| CANCELLED | &quot;cancelled&quot; |



