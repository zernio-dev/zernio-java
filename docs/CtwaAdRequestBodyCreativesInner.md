

# CtwaAdRequestBodyCreativesInner

Supply headline, body, and image/video, or exactly one existing post reference. References cannot be combined with fresh creative fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformPostId** | **String** | Messaging and CTWA only. Platform post or reel ID, the same input boostPost takes as platformPostId. Facebook IDs become object_story_id; Instagram IDs become source_instagram_media_id using the connected Instagram identity. Mutually exclusive with objectStoryId and fresh creative fields. |  [optional] |
|**existingPostId** | **String** | Alias of platformPostId, kept for existing callers. Sending both with different values is a 400. |  [optional] |
|**objectStoryId** | **String** | Messaging and CTWA only. Raw Facebook pageId_postId reference, used as object_story_id even with an Instagram account. Mutually exclusive with platformPostId and fresh creative fields. |  [optional] |
|**creativeFeatures** | [**Map&lt;String, InnerEnum&gt;**](#Map&lt;String, InnerEnum&gt;) | Replaces the top-level creativeFeatures map for this item. Omit to inherit; an empty object clears inherited enrollment choices. |  [optional] |
|**headline** | **String** |  |  [optional] |
|**body** | **String** | Primary text shown above the image / video. |  [optional] |
|**imageUrl** | **URI** | Image asset. Mutually exclusive with this entry&#39;s &#x60;video&#x60;. Required if neither &#x60;video&#x60; nor an existing post reference is supplied.  |  [optional] |
|**video** | [**CtwaAdRequestBodyCreativesInnerVideo**](CtwaAdRequestBodyCreativesInnerVideo.md) |  |  [optional] |
|**welcomeMessage** | [**CtwaAdRequestBodyCreativesInnerWelcomeMessage**](CtwaAdRequestBodyCreativesInnerWelcomeMessage.md) |  |  [optional] |



## Enum: Map&lt;String, InnerEnum&gt;

| Name | Value |
|---- | -----|
| OPT_IN | &quot;OPT_IN&quot; |
| OPT_OUT | &quot;OPT_OUT&quot; |



