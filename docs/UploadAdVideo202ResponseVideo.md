

# UploadAdVideo202ResponseVideo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Meta video id. Usable as video.id once GET /v1/ads/videos/{videoId} reports ready. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**thumbnailUrl** | **String** | Always null on 202; read it from GET /v1/ads/videos/{videoId} once ready. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PROCESSING | &quot;processing&quot; |



