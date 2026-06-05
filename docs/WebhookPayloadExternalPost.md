

# WebhookPayloadExternalPost

Webhook payload for post.external.created / post.external.updated / post.external.deleted. Fired by Zernio's background sync when it detects a natively-authored post (e.g. a Google Business Profile localPost created in the Google UI), NOT a post published through Zernio. Poll-driven (~hourly), not real-time. On post.external.deleted, post.deletedAt is populated. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**post** | [**ExternalPostWebhookPost**](ExternalPostWebhookPost.md) |  |  |
|**account** | [**WebhookPayloadReviewNewAccount**](WebhookPayloadReviewNewAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| POST_EXTERNAL_CREATED | &quot;post.external.created&quot; |
| POST_EXTERNAL_UPDATED | &quot;post.external.updated&quot; |
| POST_EXTERNAL_DELETED | &quot;post.external.deleted&quot; |



