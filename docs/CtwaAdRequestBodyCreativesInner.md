

# CtwaAdRequestBodyCreativesInner

Supply headline, body, and image/video, or exactly one existing post reference. References cannot be combined with fresh creative fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**existingPostId** | **String** | Messaging and CTWA only. Platform post or reel ID, resolved like boost platformPostId. Facebook IDs become object_story_id; Instagram IDs become source_instagram_media_id using the connected Instagram identity. Mutually exclusive with objectStoryId and fresh creative fields. |  [optional] |
|**objectStoryId** | **String** | Messaging and CTWA only. Raw Facebook pageId_postId reference, used as object_story_id even with an Instagram account. Mutually exclusive with existingPostId and fresh creative fields. |  [optional] |
|**headline** | **String** |  |  [optional] |
|**body** | **String** | Primary text shown above the image / video. |  [optional] |
|**imageUrl** | **URI** | Image asset. Mutually exclusive with this entry&#39;s &#x60;video&#x60;. Required if neither &#x60;video&#x60; nor an existing post reference is supplied.  |  [optional] |
|**video** | [**CtwaAdRequestBodyCreativesInnerVideo**](CtwaAdRequestBodyCreativesInnerVideo.md) |  |  [optional] |
|**welcomeMessage** | [**CtwaAdRequestBodyCreativesInnerWelcomeMessage**](CtwaAdRequestBodyCreativesInnerWelcomeMessage.md) |  |  [optional] |



