

# WebhookPayloadCommentCommentAttachment

Facebook only. Present on graphic-only comments (sticker, GIF, photo) that carry no text. URLs are ephemeral and may expire for Meta platforms (oe= expiry), so fetch promptly. Instagram comments do not support attachments. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | Attachment type: sticker, animated_image_share, or photo. |  |
|**imageUrl** | **String** | Rendered image/preview URL (from attachment.media.image.src). |  [optional] |
|**url** | **String** | Source URL (from attachment.url). For GIFs this is an l.facebook.com redirect. |  [optional] |



