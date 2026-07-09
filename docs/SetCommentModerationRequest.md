

# SetCommentModerationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The social account ID |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Only YouTube supports comment moderation |  |
|**moderationStatus** | [**ModerationStatusEnum**](#ModerationStatusEnum) | published approves the comment, rejected removes it, heldForReview returns it to the queue. |  |
|**banAuthor** | **Boolean** | Also ban the comment&#39;s author, auto-rejecting their future comments. Only valid when moderationStatus is \&quot;rejected\&quot;; any other pairing is a 400.  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| YOUTUBE | &quot;youtube&quot; |



## Enum: ModerationStatusEnum

| Name | Value |
|---- | -----|
| PUBLISHED | &quot;published&quot; |
| REJECTED | &quot;rejected&quot; |
| HELD_FOR_REVIEW | &quot;heldForReview&quot; |



