

# SendDiscordDirectMessageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | SocialAccount _id of the connected Discord account the bot speaks as. Caller must own the account (directly or via team membership). |  |
|**userId** | **String** | Discord snowflake ID of the recipient (15-21 digits). |  |
|**content** | **String** | Message text, up to 2,000 characters. |  [optional] |
|**embeds** | **List&lt;Object&gt;** | Up to 10 Discord embeds. Same shape as channel-post embeds (title, description, color, fields, etc.). See DiscordPlatformData.embeds for the embed object schema. |  [optional] |
|**attachments** | [**List&lt;SendDiscordDirectMessageRequestAttachmentsInner&gt;**](SendDiscordDirectMessageRequestAttachmentsInner.md) | Up to 10 media attachments. Each is &#x60;{ type: image|video|gif|document, url, filename?, mimeType?, size? }&#x60;. |  [optional] |
|**tts** | **Boolean** | Send as text-to-speech message. |  [optional] |



