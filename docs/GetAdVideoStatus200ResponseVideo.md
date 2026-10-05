

# GetAdVideoStatus200ResponseVideo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**platformStatus** | **String** | Meta&#39;s raw status.video_status, forwarded verbatim. |  |
|**processingProgress** | **Integer** | Meta&#39;s processing percentage when reported. |  |
|**error** | **String** | Meta&#39;s processing error when status is error. |  |
|**thumbnailUrl** | **String** | Meta&#39;s auto-generated poster once ready, when Meta produced one. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PROCESSING | &quot;processing&quot; |
| READY | &quot;ready&quot; |
| ERROR | &quot;error&quot; |



