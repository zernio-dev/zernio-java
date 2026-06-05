

# ExternalPostWebhookPost

Native (external) post data shared by all post.external.* payloads.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native post ID (NOT a Zernio post ID). |  |
|**platform** | **String** | Platform the post lives on (e.g. \&quot;googlebusiness\&quot;). |  |
|**accountId** | **String** | Zernio social account ID the post belongs to. |  |
|**url** | **String** | Direct URL to the post on the platform, when available. |  |
|**content** | **String** | Post text. May be empty. |  |
|**mediaType** | **String** | One of image, video, gif, document, text, carousel. |  |
|**mediaItems** | [**List&lt;ExternalPostMediaItem&gt;**](ExternalPostMediaItem.md) |  |  |
|**thumbnailUrl** | **String** |  |  |
|**publishedAt** | **OffsetDateTime** |  |  |
|**source** | [**SourceEnum**](#SourceEnum) | Always \&quot;external\&quot; — distinguishes these from Zernio-originated post.* events. |  |
|**deletedAt** | **OffsetDateTime** | Detection time of deletion. Present on post.external.deleted; null/absent otherwise. |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| EXTERNAL | &quot;external&quot; |



