

# CommentAutomationAudience

Who a comment automation answers. Instagram only - Meta exposes the follow relationship on no other platform, and only for people who have MESSAGED the account (a comment grants no consent). `whenUnknown` is therefore the important setting: it decides what happens for a first-time commenter. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**followerStatus** | [**FollowerStatusEnum**](#FollowerStatusEnum) |  |  [optional] |
|**minFollowerCount** | **Integer** | Skip commenters with fewer followers than this. Omit for no size rule. |  [optional] |
|**whenUnknown** | [**WhenUnknownEnum**](#WhenUnknownEnum) | What to do when Instagram will not reveal the follow relationship.   * &#x60;send&#x60; (default) - deliver the DM anyway (fails open).   * &#x60;skip&#x60; - stay silent.   * &#x60;verify&#x60; - send &#x60;followGate.message&#x60; with a confirm button. Tapping it is a     message, which grants consent, so the re-check on the tap resolves and the     real DM (or &#x60;followGate.notFollowingMessage&#x60;) follows automatically.  |  [optional] |



## Enum: FollowerStatusEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| FOLLOWER | &quot;follower&quot; |
| NON_FOLLOWER | &quot;non_follower&quot; |



## Enum: WhenUnknownEnum

| Name | Value |
|---- | -----|
| SEND | &quot;send&quot; |
| SKIP | &quot;skip&quot; |
| VERIFY | &quot;verify&quot; |



