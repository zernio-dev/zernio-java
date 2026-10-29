

# WebhookPayloadAccountAdsSyncRecovered

Webhook payload for `account.ads.sync_recovered` events. Fired once when an ad account previously reported by `account.ads.sync_failed` syncs successfully again. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookAdsSyncAccount**](WebhookAdsSyncAccount.md) |  |  |
|**adAccount** | [**WebhookAdsSyncAdAccount**](WebhookAdsSyncAdAccount.md) |  |  |
|**sync** | [**WebhookPayloadAccountAdsSyncRecoveredSync**](WebhookPayloadAccountAdsSyncRecoveredSync.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event. Retries and redeliveries keep the original value. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| ACCOUNT_ADS_SYNC_RECOVERED | &quot;account.ads.sync_recovered&quot; |



