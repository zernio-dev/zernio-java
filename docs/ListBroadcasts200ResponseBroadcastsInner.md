

# ListBroadcasts200ResponseBroadcastsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountName** | **String** | Display name of the sending account |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**messagePreview** | **String** | Template name or message text snippet |  [optional] |
|**scheduledAt** | **OffsetDateTime** |  |  [optional] |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**completedAt** | **OffsetDateTime** |  |  [optional] |
|**recipientCount** | **Integer** |  |  [optional] |
|**sentCount** | **Integer** |  |  [optional] |
|**deliveredCount** | **Integer** |  |  [optional] |
|**readCount** | **Integer** |  |  [optional] |
|**failedCount** | **Integer** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| SENDING | &quot;sending&quot; |
| COMPLETED | &quot;completed&quot; |
| FAILED | &quot;failed&quot; |
| CANCELLED | &quot;cancelled&quot; |



