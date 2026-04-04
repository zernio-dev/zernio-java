

# CreateInboxConversationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The social account ID to send from |  |
|**participantId** | **String** | Twitter numeric user ID of the recipient. Provide either this or &#x60;participantUsername&#x60;. |  [optional] |
|**participantUsername** | **String** | Twitter username (with or without @) of the recipient. Resolved to a user ID via lookup. Provide either this or &#x60;participantId&#x60;. |  [optional] |
|**message** | **String** | Text content of the message. At least one of &#x60;message&#x60; or attachment is required. |  [optional] |
|**skipDmCheck** | **Boolean** | Skip the &#x60;receives_your_dm&#x60; eligibility check before sending. Use if you have already verified the recipient accepts DMs. |  [optional] |



