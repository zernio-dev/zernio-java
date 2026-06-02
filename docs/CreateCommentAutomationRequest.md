

# CreateCommentAutomationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**accountId** | **String** | Instagram or Facebook account ID |  |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | What fires the automation. &#39;comment&#39; (keyword comment on a post) or &#39;story_reply&#39; (keyword reply to an Instagram story). For &#39;story_reply&#39;, platformPostId is the story media id (omit for any story). |  [optional] |
|**platformPostId** | **String** | Platform media/post ID (or story media id when trigger&#x3D;story_reply). Omit for an account-wide (any-post / any-story) automation. |  [optional] |
|**postId** | **String** | Zernio post ID. Required only when also targeting a specific post via platformPostId. |  [optional] |
|**postTitle** | **String** | Post content snippet for display |  [optional] |
|**name** | **String** | Automation label |  |
|**keywords** | **List&lt;String&gt;** | Trigger keywords (empty &#x3D; any comment triggers) |  [optional] |
|**matchMode** | [**MatchModeEnum**](#MatchModeEnum) |  |  [optional] |
|**dmMessage** | **String** | DM text to send to commenter. Max 640 chars when buttons are set, otherwise ~1000. |  |
|**buttons** | [**List&lt;DmButton&gt;**](DmButton.md) | Optional inline DM buttons (1-3). Phone buttons are Facebook-only. Omit or pass [] for a plain-text DM. |  [optional] |
|**commentReply** | **String** | Optional public reply to the comment |  [optional] |
|**linkTracking** | **Boolean** | Wrap link buttons in the DM in a tracked redirect so clicks are counted (Link Clicks / CTR). Pass false to send links exactly as written. Defaults to on. |  [optional] |
|**clickTag** | **String** | Optional tag applied to a contact when they click a tracked link (requires linkTracking). Lets you segment clickers for broadcasts/sequences. |  [optional] |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| COMMENT | &quot;comment&quot; |
| STORY_REPLY | &quot;story_reply&quot; |



## Enum: MatchModeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;exact&quot; |
| CONTAINS | &quot;contains&quot; |



