

# DiscordPlatformData

Discord message settings. Supports plain text (2,000 chars), rich embeds (up to 10), native polls, forum posts, threads, and announcement crossposts. Media attachments support images (JPEG, PNG, GIF, WebP), videos (MP4), and documents (up to 10 files, 25 MB each). Webhook identity (username + avatar) can be customized per-account via PATCH /v1/connect/discord or per-post via webhookUsername/webhookAvatarUrl. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelId** | **String** | Target channel snowflake ID. Determines which channel in the connected server receives the message. |  |
|**embeds** | [**List&lt;DiscordPlatformDataEmbedsInner&gt;**](DiscordPlatformDataEmbedsInner.md) | Up to 10 Discord embed objects (combined max 6,000 characters across all embeds). Sent alongside or instead of plain-text content. |  [optional] |
|**poll** | [**DiscordPlatformDataPoll**](DiscordPlatformDataPoll.md) |  |  [optional] |
|**crosspost** | **Boolean** | Auto-crosspost to every server following this announcement channel (type 5). No-op for regular text channels. |  [optional] |
|**forumThreadName** | **String** | Thread title for forum channel posts (type 15). Required when posting to a forum channel. |  [optional] |
|**forumAppliedTags** | **List&lt;String&gt;** | Tag snowflake IDs to apply to forum posts. Max 5 tags. |  [optional] |
|**threadFromMessage** | [**DiscordPlatformDataThreadFromMessage**](DiscordPlatformDataThreadFromMessage.md) |  |  [optional] |
|**tts** | **Boolean** | Send as text-to-speech message. Discord reads the message aloud in the channel. |  [optional] |
|**webhookUsername** | **String** | Override the webhook display name for this post only (1-80 chars). Falls back to the account-level default set via PATCH /v1/connect/discord. |  [optional] |
|**webhookAvatarUrl** | **String** | Override the webhook avatar URL for this post only. Falls back to the account-level default. |  [optional] |



