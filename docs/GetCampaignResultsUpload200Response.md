

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



