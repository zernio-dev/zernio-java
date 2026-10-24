

# FacebookVisitorPostMedia

Media of the first attachment, in the same shape as Facebook Page posts. Null when the post has no attachment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) |  |  |
|**thumbnailUrl** | **String** | Temporary CDN URL of the cover image. Empty when there is none. |  |
|**mediaItems** | [**List&lt;FacebookVisitorPostMediaMediaItemsInner&gt;**](FacebookVisitorPostMediaMediaItemsInner.md) |  |  |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| CAROUSEL | &quot;carousel&quot; |
| TEXT | &quot;text&quot; |



