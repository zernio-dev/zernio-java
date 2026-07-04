

# WebhookPayloadPostPlatform

Webhook payload for the per-platform terminal events `post.platform.published` and `post.platform.failed`, and for `post.tiktok.url_resolved` (same shape, fired when a published TikTok post's public URL is backfilled). Terminal events fire once per platform target inside a post as that platform reaches a terminal state (published or permanent failure). The `post` envelope mirrors the shape of `WebhookPayloadPost` so consumers can reuse rendering logic; the `platform` block identifies which specific platform transitioned; the `account` block identifies the connected social account behind that platform-write. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**post** | [**WebhookPayloadPostPlatformPost**](WebhookPayloadPostPlatformPost.md) |  |  |
|**platform** | [**WebhookPayloadPostPlatformPlatform**](WebhookPayloadPostPlatformPlatform.md) |  |  |
|**account** | [**WebhookPayloadPostPlatformAccount**](WebhookPayloadPostPlatformAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| POST_PLATFORM_PUBLISHED | &quot;post.platform.published&quot; |
| POST_PLATFORM_FAILED | &quot;post.platform.failed&quot; |
| POST_TIKTOK_URL_RESOLVED | &quot;post.tiktok.url_resolved&quot; |



