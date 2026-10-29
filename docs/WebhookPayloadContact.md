

# WebhookPayloadContact

Webhook payload for contact.updated and contact.deleted, fired after a provider contacts sync (Google Contacts, Outlook) changed a contact. Read the contact with `GET /v1/contacts/{id}`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadCalendarEventAccount**](WebhookPayloadCalendarEventAccount.md) |  |  |
|**contact** | [**WebhookPayloadContactContact**](WebhookPayloadContactContact.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CONTACT_UPDATED | &quot;contact.updated&quot; |
| CONTACT_DELETED | &quot;contact.deleted&quot; |



