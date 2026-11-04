

# WebhookPayloadAutomationAction

Webhook payload for `automation.action.applied`, `automation.action.failed` and `automation.action.unknown`: one change an automation made or tried.  Sent once per action as it settles. A refusal decided before any platform call (no live ads, a budget already at its limit) arrives as `automation.action.failed` with `status: skipped`. An `unknown` action is read back by the next check and sent again with its final status. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**automation** | [**WebhookAutomationRef**](WebhookAutomationRef.md) |  |  |
|**accountId** | **String** | The connected account the automation acts on. |  |
|**checkId** | **String** | The check that recorded the action. |  |
|**action** | [**WebhookPayloadAutomationActionAction**](WebhookPayloadAutomationActionAction.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| AUTOMATION_ACTION_APPLIED | &quot;automation.action.applied&quot; |
| AUTOMATION_ACTION_FAILED | &quot;automation.action.failed&quot; |
| AUTOMATION_ACTION_UNKNOWN | &quot;automation.action.unknown&quot; |



