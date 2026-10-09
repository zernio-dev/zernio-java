

# WebhookPayloadAccountAdsSyncFailed

Webhook payload for `account.ads.sync_failed` events. Fired once per ad account when its ads stop syncing: no successful sync for 24 hours, or every live ad in it at the retry cap. It does not fire again for the same ad account until `account.ads.sync_recovered`. Metrics for the ad account are stale meanwhile. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. |  |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookAdsSyncAccount**](WebhookAdsSyncAccount.md) |  |  |
|**adAccount** | [**WebhookAdsSyncAdAccount**](WebhookAdsSyncAdAccount.md) |  |  |
|**sync** | [**WebhookPayloadAccountAdsSyncFailedSync**](WebhookPayloadAccountAdsSyncFailedSync.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event. Retries and redeliveries keep the original value. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| ACCOUNT_ADS_SYNC_FAILED | &quot;account.ads.sync_failed&quot; |



