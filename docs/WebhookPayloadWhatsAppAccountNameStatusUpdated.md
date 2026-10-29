

# WebhookPayloadWhatsAppAccountNameStatusUpdated

Webhook payload for the `whatsapp.account.name_status_updated` event, fired when Meta finishes reviewing a WhatsApp display-name change on a connected number. Maps Meta's `phone_number_name_update` WABA webhook field onto our event envelope.  Fires only for a review outcome (APPROVED, DECLINED, PENDING_REVIEW). A name applied without review reports `name_status: AVAILABLE_WITHOUT_REVIEW` on the phone node instead; Meta never sends this webhook field for that case. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadWhatsAppTemplateStatusUpdatedAccount**](WebhookPayloadWhatsAppTemplateStatusUpdatedAccount.md) |  |  |
|**name** | [**WebhookPayloadWhatsAppAccountNameStatusUpdatedName**](WebhookPayloadWhatsAppAccountNameStatusUpdatedName.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WHATSAPP_ACCOUNT_NAME_STATUS_UPDATED | &quot;whatsapp.account.name_status_updated&quot; |



