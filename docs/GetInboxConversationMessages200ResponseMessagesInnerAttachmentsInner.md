

# GetInboxConversationMessages200ResponseMessagesInnerAttachmentsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**originalType** | **String** | Instagram and Facebook only, and present only when it differs from &#x60;type&#x60;. Meta&#39;s own type before normalization: &#x60;ig_reel&#x60; and &#x60;reel&#x60; become &#x60;video&#x60;, while &#x60;ig_post&#x60;, &#x60;post&#x60;, &#x60;ig_story&#x60; and &#x60;story_mention&#x60; become &#x60;share&#x60;. A story mention is &#x60;type: \&quot;share\&quot;&#x60; with &#x60;originalType: \&quot;story_mention\&quot;&#x60;; render on this field, since &#x60;share&#x60; alone is ambiguous. |  [optional] |
|**url** | **String** | Direct media link. On Instagram and Facebook this is a signed Meta CDN url that EXPIRES: use it now, do not store it. Persist &#x60;refreshUrl&#x60; instead. |  [optional] |
|**refreshUrl** | **String** | Instagram and Facebook only. Endpoint that resolves this attachment to a working url every time, re-minting it from Meta when the stored one has expired. Safe to store and render indefinitely. |  [optional] |
|**filename** | **String** |  |  [optional] |
|**previewUrl** | **String** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| AUDIO | &quot;audio&quot; |
| FILE | &quot;file&quot; |
| STICKER | &quot;sticker&quot; |
| SHARE | &quot;share&quot; |



