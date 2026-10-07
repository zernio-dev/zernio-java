

# ListInboxConversationAnalytics200ResponseItemsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationId** | **String** | The platformConversationId. A thread whose events were logged under both its ids comes back as one row. |  [optional] |
|**mongoId** | **String** | The Zernio conversation id, when a matching conversation exists |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**participantName** | **String** |  |  [optional] |
|**participantUsername** | **String** |  |  [optional] |
|**participantPicture** | **String** |  |  [optional] |
|**lastMessage** | **String** | Cached preview from the Conversation doc |  [optional] |
|**totalMessages** | **Integer** |  |  [optional] |
|**received** | **Integer** |  |  [optional] |
|**sent** | **Integer** |  |  [optional] |
|**read** | **Integer** |  |  [optional] |
|**failed** | **Integer** |  |  [optional] |
|**firstMessageAt** | **OffsetDateTime** |  |  [optional] |
|**lastMessageAt** | **OffsetDateTime** |  |  [optional] |



