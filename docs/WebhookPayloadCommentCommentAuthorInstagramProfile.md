

# WebhookPayloadCommentCommentAuthorInstagramProfile

Instagram only, best-effort. Present ONLY for commenters who have messaged the account before: Meta gates the follow relationship behind messaging consent, and commenting does not grant it. Absent otherwise - treat a missing object as \"unknown\", never as \"not a follower\". To check on demand, call GET /v1/accounts/{accountId}/follow-status/{userId}. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isFollower** | **Boolean** | The commenter follows this account. |  [optional] |
|**isFollowing** | **Boolean** | This account follows the commenter. |  [optional] |
|**followerCount** | **Integer** |  |  [optional] |
|**isVerified** | **Boolean** |  |  [optional] |



