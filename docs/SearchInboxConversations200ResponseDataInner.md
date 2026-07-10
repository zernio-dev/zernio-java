

# SearchInboxConversations200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversation** | [**SearchInboxConversations200ResponseDataInnerConversation**](SearchInboxConversations200ResponseDataInnerConversation.md) |  |  [optional] |
|**matchCount** | **Integer** | Number of matching messages in this conversation. 0 when the conversation matched only on contact identity (name, username, or phone number), not on message text. |  [optional] |
|**matches** | [**List&lt;SearchInboxConversations200ResponseDataInnerMatchesInner&gt;**](SearchInboxConversations200ResponseDataInnerMatchesInner.md) | Up to 3 most-recent matching messages (empty for an identity-only match) |  [optional] |



