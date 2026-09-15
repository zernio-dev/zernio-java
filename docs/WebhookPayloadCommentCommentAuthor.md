

# WebhookPayloadCommentCommentAuthor


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Author&#39;s platform ID |  |
|**username** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**picture** | **String** |  |  [optional] |
|**isOwnAccount** | **Boolean** | True when this comment was authored by the connected account itself. Populated on the Instagram and Facebook realtime webhooks (Meta re-delivers the account&#39;s own replies as comments events) and on TikTok, where it is inferred: comments created through this API are always flagged, and once the account&#39;s own author identifier is known (from one of those or from a comments listing) every author is compared against it. Absent means not evaluated, never \&quot;not the account\&quot;. |  [optional] |
|**instagramProfile** | [**WebhookPayloadCommentCommentAuthorInstagramProfile**](WebhookPayloadCommentCommentAuthorInstagramProfile.md) |  |  [optional] |



