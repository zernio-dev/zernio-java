

# InboxWebhookConversationDetail

The conversation object included in conversation lifecycle webhook payloads (conversation.started, conversation.control_changed).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The platform&#39;s conversation id, equal to &#x60;conversation.platformConversationId&#x60; on inbox webhooks (whose &#x60;conversation.id&#x60; is Zernio&#39;s internal id). Both are accepted by the conversation endpoints. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**platformConversationId** | **String** | Same value as &#x60;id&#x60;. |  |
|**participantId** | **String** | Contact&#39;s platform identifier (IGSID, PSID, wa_id, etc.) |  [optional] |
|**participantName** | **String** |  |  |
|**participantUsername** | **String** | Contact&#39;s handle when the platform exposes one |  [optional] |
|**participantPicture** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**contactId** | **String** | Zernio CRM Contact ID for the participant, when one exists. Resolved by joining &#x60;participantId&#x60; to the ContactChannel collection (same join used by message.*, reaction.received, and call.* webhooks). Best-effort: omitted when no channel matches or &#x60;participantId&#x60; is absent. Lets integrators seed the CRM straight from &#x60;conversation.started&#x60; without waiting for the first &#x60;message.*&#x60; event.  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| TELEGRAM | &quot;telegram&quot; |
| WHATSAPP | &quot;whatsapp&quot; |
| TWITTER | &quot;twitter&quot; |
| REDDIT | &quot;reddit&quot; |
| BLUESKY | &quot;bluesky&quot; |
| SMS | &quot;sms&quot; |
| SLACK | &quot;slack&quot; |
| TIKTOK | &quot;tiktok&quot; |
| IMESSAGE | &quot;imessage&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



