

# GetCommentAutomation200ResponseLogsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**commentId** | **String** |  |  [optional] |
|**commenterId** | **String** |  |  [optional] |
|**commenterName** | **String** |  |  [optional] |
|**commentText** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**error** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SENT | &quot;sent&quot; |
| FAILED | &quot;failed&quot; |
| SKIPPED | &quot;skipped&quot; |



