

# CreateInboxConversation201ResponseData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageId** | **String** | Platform message ID (dm_event_id) |  [optional] |
|**conversationId** | **String** | Platform conversation ID (dm_conversation_id). For WhatsApp, this is Zernio&#39;s internal conversation id (24-character hex) which matches the id returned by the list-conversations endpoint and the conversationId in the message.received and conversation.started webhooks; use it to correlate the created thread with inbound events. |  [optional] |
|**participantId** | **String** | Twitter numeric user ID of the recipient |  [optional] |
|**participantName** | **String** | Display name of the recipient |  [optional] |
|**participantUsername** | **String** | Twitter username of the recipient |  [optional] |



