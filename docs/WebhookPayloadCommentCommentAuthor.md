

# WebhookPayloadCommentCommentAuthor


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Author&#39;s platform ID |  |
|**username** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**picture** | **String** |  |  [optional] |
|**isOwnAccount** | **Boolean** | True when this comment was authored by the connected account itself (Meta re-delivers the account&#39;s own replies as comments events). Populated on the Instagram and Facebook realtime webhooks only; absent means not evaluated, never \&quot;not the account\&quot;. |  [optional] |
|**instagramProfile** | [**WebhookPayloadCommentCommentAuthorInstagramProfile**](WebhookPayloadCommentCommentAuthorInstagramProfile.md) |  |  [optional] |



