

# GetEvent200ResponseDeliveriesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**destinationId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**attempt** | **Integer** | Send attempt (1 &#x3D; the first). |  [optional] |
|**error** | **String** |  |  [optional] |
|**errorCode** | **String** |  |  [optional] |
|**sentAt** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| METAADS | &quot;metaads&quot; |
| GOOGLEADS | &quot;googleads&quot; |
| LINKEDINADS | &quot;linkedinads&quot; |
| TIKTOKADS | &quot;tiktokads&quot; |
| OPENAIADS | &quot;openaiads&quot; |
| PINTERESTADS | &quot;pinterestads&quot; |
| REDDITADS | &quot;redditads&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SENT | &quot;sent&quot; |
| RETRYING | &quot;retrying&quot; |
| FAILED | &quot;failed&quot; |



