

# SearchInboxConversations200ResponseDataInnerConversation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Conversation ID, usable with the conversation messages endpoints |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**participantName** | **String** |  |  [optional] |
|**participantUsername** | **String** |  |  [optional] |
|**participantPicture** | **String** |  |  [optional] |
|**businessScopedUserId** | **String** | WhatsApp only. Meta business-scoped user ID (BSUID), the stable identity anchor; present when Meta has sent it for this participant. |  [optional] |
|**whatsappUsername** | **String** | WhatsApp only. The participant&#39;s WhatsApp username (e.g. &#x60;jane.shop&#x60;, no leading @). Not a stable identifier, because users can change it: useful for display, not recommended as an identity anchor. Captured from inbound messages, so older threads fill in on their next inbound. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**lastMessage** | **String** | The conversation&#39;s most recent message preview |  [optional] |
|**lastMessageAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



