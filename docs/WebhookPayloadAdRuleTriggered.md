

# WebhookPayloadAdRuleTriggered

Webhook payload for the `ad_rule.triggered` event. Ad rules are in closed beta: the event only fires for accounts in the ad rules pilot.  Fires when a scheduled ad rule run finds campaigns or ad sets that meet every condition of the rule. Each object is announced at most once per rule cooldown, so `objects` lists only the objects the run acted on, never the ones still in cooldown. A run where every matching object is still in cooldown sends nothing. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Present on every event tied to a profile and absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once. Use it to route the event to your tenant without storing Zernio profile ids. |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookAdsAccount**](WebhookAdsAccount.md) |  |  |
|**rule** | [**WebhookPayloadAdRuleTriggeredRule**](WebhookPayloadAdRuleTriggeredRule.md) |  |  |
|**run** | [**WebhookPayloadAdRuleTriggeredRun**](WebhookPayloadAdRuleTriggeredRun.md) |  |  |
|**objects** | [**List&lt;WebhookPayloadAdRuleTriggeredObjectsInner&gt;**](WebhookPayloadAdRuleTriggeredObjectsInner.md) | The campaigns or ad sets this run acted on, at the rule&#39;s &#x60;level&#x60;. Objects still in cooldown are left out. |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| AD_RULE_TRIGGERED | &quot;ad_rule.triggered&quot; |



