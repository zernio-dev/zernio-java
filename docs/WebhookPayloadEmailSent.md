

# WebhookPayloadEmailSent

Webhook payload for email.sent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadCalendarEventAccount**](WebhookPayloadCalendarEventAccount.md) |  |  |
|**source** | [**SourceEnum**](#SourceEnum) |  |  |
|**email** | [**WebhookPayloadEmailSentEmail**](WebhookPayloadEmailSentEmail.md) |  |  |
|**draftId** | **String** | The draft it was sent from (&#x60;source: draft&#x60;, or a scheduled draft). |  [optional] |
|**scheduleId** | **String** | The scheduled send (&#x60;source: scheduled&#x60;). |  [optional] |
|**replyToMessageId** | **String** |  |  [optional] |
|**forwardedFrom** | **String** |  |  [optional] |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| EMAIL_SENT | &quot;email.sent&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| SEND | &quot;send&quot; |
| REPLY | &quot;reply&quot; |
| FORWARD | &quot;forward&quot; |
| DRAFT | &quot;draft&quot; |
| SCHEDULED | &quot;scheduled&quot; |



