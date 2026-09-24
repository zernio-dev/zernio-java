

# GetInboxConversationMessages200ResponseMessagesInnerStoryReply

Instagram only. Present when the message replies to one of the account's stories. Also set on history imported after connecting, read off Meta's `story.reply_to`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storyId** | **String** | The Instagram story ID the user replied to. |  [optional] |
|**storyUrl** | **String** | Meta CDN URL for the story media. Expires roughly 24 hours after the story posted; fetch promptly or treat 404s as expected. |  [optional] |



