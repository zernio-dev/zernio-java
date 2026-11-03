

# GetCampaignResultsUpload200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**uploadId** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**source** | [**SourceEnum**](#SourceEnum) |  |  |
|**rowsReceived** | **Integer** |  |  |
|**rowsMatched** | **Integer** |  |  |
|**rowsUnmatched** | **Integer** |  |  |
|**unmatched** | [**List&lt;GetCampaignResultsUpload200ResponseUnmatchedInner&gt;**](GetCampaignResultsUpload200ResponseUnmatchedInner.md) |  |  |
|**failureReason** | [**FailureReasonEnum**](#FailureReasonEnum) | Set when &#x60;status&#x60; is &#x60;failed&#x60;. &#x60;queue_unavailable&#x60;: the upload could not be queued. &#x60;processing_failed&#x60;: its rows could not be stored after several retries. Both are on our side. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**completedAt** | **OffsetDateTime** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| DONE | &quot;done&quot; |
| FAILED | &quot;failed&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| API | &quot;api&quot; |
| CSV | &quot;csv&quot; |
| HUBSPOT | &quot;hubspot&quot; |



## Enum: FailureReasonEnum

| Name | Value |
|---- | -----|
| QUEUE_UNAVAILABLE | &quot;queue_unavailable&quot; |
| PROCESSING_FAILED | &quot;processing_failed&quot; |



