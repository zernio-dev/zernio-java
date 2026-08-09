

# LikeInboxCommentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The social account ID |  |
|**reactionType** | [**ReactionTypeEnum**](#ReactionTypeEnum) | (LinkedIn only) Reaction to create. Defaults to LIKE; ignored on other platforms. |  [optional] |
|**cid** | **String** | (Bluesky only) Content identifier for the comment |  [optional] |



## Enum: ReactionTypeEnum

| Name | Value |
|---- | -----|
| LIKE | &quot;LIKE&quot; |
| PRAISE | &quot;PRAISE&quot; |
| EMPATHY | &quot;EMPATHY&quot; |
| INTEREST | &quot;INTEREST&quot; |
| APPRECIATION | &quot;APPRECIATION&quot; |
| ENTERTAINMENT | &quot;ENTERTAINMENT&quot; |



