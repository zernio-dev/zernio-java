

# CreateCommentAutomationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**accountId** | **String** | Instagram or Facebook account ID |  |
|**platformPostId** | **String** | Platform media/post ID. Omit for an account-wide (any-post) automation. |  [optional] |
|**postId** | **String** | Zernio post ID. Required only when also targeting a specific post via platformPostId. |  [optional] |
|**postTitle** | **String** | Post content snippet for display |  [optional] |
|**name** | **String** | Automation label |  |
|**keywords** | **List&lt;String&gt;** | Trigger keywords (empty &#x3D; any comment triggers) |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) |  |  [optional] |
|**dmMessage** | **String** | DM text to send to commenter. Max 640 chars when buttons are set, otherwise ~1000. |  |
|**buttons** | [**List&lt;DmButton&gt;**](DmButton.md) | Optional inline DM buttons (1-3). Phone buttons are Facebook-only. Omit or pass [] for a plain-text DM. |  [optional] |
|**commentReply** | **String** | Optional public reply to the comment |  [optional] |



## Enum: MatchModeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;exact&quot; |
| CONTAINS | &quot;contains&quot; |



