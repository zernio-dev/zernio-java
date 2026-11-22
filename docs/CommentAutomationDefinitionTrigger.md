

# CommentAutomationDefinitionTrigger


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;comment.keyword&#x60; for a comment on a post or reel. The &#x60;comment.received&#x60; event starts an event automation, not comment to DM. |  |
|**profileId** | **String** |  |  |
|**accountId** | **String** | The account it answers on, on the profile. It cannot change once saved. |  |
|**platformPostId** | **String** | The platform post or story it answers. Null answers every one. One active automation per post. |  [optional] |
|**postId** | **String** | A Zernio post. A scheduled one is answered once it publishes. |  [optional] |
|**postTitle** | **String** |  |  [optional] |
|**filter** | [**CommentAutomationFilter**](CommentAutomationFilter.md) |  |  |
|**entry** | **List&lt;String&gt;** | The nodes a run starts at. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMMENT_KEYWORD | &quot;comment.keyword&quot; |
| COMMENT_LIVE | &quot;comment.live&quot; |
| STORY_REPLY | &quot;story.reply&quot; |
| STORY_MENTION | &quot;story.mention&quot; |



