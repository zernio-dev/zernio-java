

# WebhookPayloadPostTrackingCompletedWindow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**startsAt** | **OffsetDateTime** |  |  |
|**endsAt** | **OffsetDateTime** |  |  |
|**finalReadAt** | **OffsetDateTime** |  |  |
|**completionReason** | [**CompletionReasonEnum**](#CompletionReasonEnum) |  |  |



## Enum: CompletionReasonEnum

| Name | Value |
|---- | -----|
| FINAL_READ | &quot;final_read&quot; |
| UNREACHABLE | &quot;unreachable&quot; |
| POST_DELETED | &quot;post_deleted&quot; |



