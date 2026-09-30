

# WebhookPayloadWhatsAppContactIdentityChanged

Webhook payload for the `whatsapp.contact.identity_changed` event. Fired when Meta reports that a WhatsApp user is now known by a different identifier: a `system` message of type `user_changed_number`, `user_changed_user_id` or `user_identity_changed`, or a `user_id_update` webhook (BSUID regenerated). Zernio re-keys the inbox conversation and contact channel before firing. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadWhatsAppContactIdentityChangedAccount**](WebhookPayloadWhatsAppContactIdentityChangedAccount.md) |  |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Which Meta signal reported the change. &#x60;user_changed_number&#x60;: new phone number. &#x60;user_changed_user_id&#x60; and &#x60;user_id_update&#x60;: new BSUID. |  |
|**previous** | [**WhatsAppContactIdentity**](WhatsAppContactIdentity.md) |  |  |
|**current** | [**WhatsAppContactIdentity**](WhatsAppContactIdentity.md) |  |  |
|**contactId** | **String** | Zernio contact id matched on the new identity, null when none exists yet. |  |
|**conversationId** | **String** | Zernio inbox conversation that was re-keyed, null when there was none. |  |
|**changedAt** | **OffsetDateTime** | When Meta reported the change. |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WHATSAPP_CONTACT_IDENTITY_CHANGED | &quot;whatsapp.contact.identity_changed&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| USER_CHANGED_NUMBER | &quot;user_changed_number&quot; |
| USER_CHANGED_USER_ID | &quot;user_changed_user_id&quot; |
| USER_IDENTITY_CHANGED | &quot;user_identity_changed&quot; |
| USER_ID_UPDATE | &quot;user_id_update&quot; |



