

# WebhookPayloadAutomationAlert

Webhook payload for `automation.alert.opened`, `automation.alert.escalated` and `automation.alert.resolved`: an alert episode of an automation with a lifecycle (an ad rule's `lifecycle`).  Sent as soon as the check records the change; a resolve that a pause or reactivation causes is sent once it applies. A streak that never opened sends nothing.  Alerts closed outside a check (the rule turned off, deleted or its `lifecycle` removed between checks, or the daily cleanup) are not announced. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**automation** | [**WebhookAutomationRef**](WebhookAutomationRef.md) |  |  |
|**accountId** | **String** | The connected account the automation acts on. |  |
|**checkId** | **String** | The check that moved the alert. |  |
|**alert** | [**WebhookPayloadAutomationAlertAlert**](WebhookPayloadAutomationAlertAlert.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| AUTOMATION_ALERT_OPENED | &quot;automation.alert.opened&quot; |
| AUTOMATION_ALERT_ESCALATED | &quot;automation.alert.escalated&quot; |
| AUTOMATION_ALERT_RESOLVED | &quot;automation.alert.resolved&quot; |



