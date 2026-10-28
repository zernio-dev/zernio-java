

# TrackingWindow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**postId** | **String** | The external post being tracked |  |
|**accountId** | **String** |  |  |
|**platform** | **String** |  |  |
|**platformPostId** | **String** | The post&#39;s id on the platform |  |
|**startsAt** | **OffsetDateTime** |  |  |
|**endsAt** | **OffsetDateTime** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**finalReadAt** | **OffsetDateTime** | When the closing read ran. Null until then. |  |
|**completionReason** | [**CompletionReasonEnum**](#CompletionReasonEnum) | How the window closed. Null while it is open. |  |
|**requestedBy** | **String** |  |  |
|**latest** | [**TrackingWindowLatest**](TrackingWindowLatest.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| COMPLETING | &quot;completing&quot; |
| COMPLETED | &quot;completed&quot; |
| CANCELLED | &quot;cancelled&quot; |



## Enum: CompletionReasonEnum

| Name | Value |
|---- | -----|
| FINAL_READ | &quot;final_read&quot; |
| UNREACHABLE | &quot;unreachable&quot; |
| POST_DELETED | &quot;post_deleted&quot; |
| CANCELLED | &quot;cancelled&quot; |



