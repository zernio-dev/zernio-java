

# ListSequences200ResponseSequencesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountName** | **String** | Display name of the sending account |  [optional] |
|**messagePreview** | **String** | First step template name or message text snippet |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**stepsCount** | **Integer** |  |  [optional] |
|**exitOnReply** | **Boolean** |  |  [optional] |
|**exitOnUnsubscribe** | **Boolean** |  |  [optional] |
|**totalEnrolled** | **Integer** |  |  [optional] |
|**totalCompleted** | **Integer** |  |  [optional] |
|**totalExited** | **Integer** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



