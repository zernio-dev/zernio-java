

# CommentAutomationActions

Actions taken on the matched comment itself (comment trigger only; ignored on the story-reply and DM doors). They never block or fail the DM: when one cannot run, the log row says why (`likeSkipped`, `hideSkipped`). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**likeComment** | **Boolean** | Like the comment as the account. Facebook always; Instagram only for accounts connected through Facebook Login and allowlisted for likes while Meta reviews the permission. Otherwise the like is skipped and logged. |  [optional] |
|**hideComment** | **Boolean** | Hide the comment once the first DM has been attempted, so the private reply is never sent to an already hidden comment. |  [optional] |



