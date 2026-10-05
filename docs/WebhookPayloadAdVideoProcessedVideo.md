

# WebhookPayloadAdVideoProcessedVideo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Meta video id, as returned by the 202 upload response. |  |
|**platformAdAccountId** | **String** | Meta ad account id (act_&lt;n&gt;) the video was uploaded to. |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;ready&#x60;: usable as &#x60;video.id&#x60; on the create endpoints. &#x60;error&#x60;: Meta could not process it; upload again. |  |
|**error** | **String** | Meta&#39;s processing error when status is &#x60;error&#x60;, otherwise null. |  |
|**thumbnailUrl** | **String** | Meta&#39;s auto-generated poster when status is &#x60;ready&#x60; and Meta produced one, otherwise null. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;ready&quot; |
| ERROR | &quot;error&quot; |



