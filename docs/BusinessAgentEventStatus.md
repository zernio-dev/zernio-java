

# BusinessAgentEventStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**eventType** | **String** |  |  |
|**errorMessage** | **String** |  |  [optional] |
|**skippedReason** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| REQUEST_RECEIVED | &quot;request_received&quot; |
| PROCESSING | &quot;processing&quot; |
| SENT | &quot;sent&quot; |
| FAILED | &quot;failed&quot; |
| SKIPPED | &quot;skipped&quot; |
| SUCCESS | &quot;success&quot; |



