

# VoteRedditThingRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**thingId** | **String** | Reddit fullname of the target. Prefix \&quot;t3_\&quot; for a post and \&quot;t1_\&quot; for a comment. A bare id with no prefix is treated as a post (\&quot;t3_\&quot;).  |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) | 1 to upvote, -1 to downvote, 0 to clear an existing vote |  |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_0 | 0 |
| NUMBER_MINUS_1 | -1 |



