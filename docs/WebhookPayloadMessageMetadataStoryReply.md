

# WebhookPayloadMessageMetadataStoryReply

Instagram only. Populated when an IG user replies to one of the account's stories (Meta `messaging_story_replies`). Mutually exclusive in practice with `isStoryMention`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storyId** | **String** | The Instagram story ID the user replied to. |  |
|**storyUrl** | **String** | Meta CDN URL for the story media. Expires approximately 24 hours after the story posted; consumers must fetch promptly or treat 404s as expected.  |  [optional] |



