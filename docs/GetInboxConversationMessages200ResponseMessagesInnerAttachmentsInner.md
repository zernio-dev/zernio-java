

# GetInboxConversationMessages200ResponseMessagesInnerAttachmentsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
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



