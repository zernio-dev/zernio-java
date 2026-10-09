

# WebhookPayloadAccountAdsInitialSyncCompleted

Webhook payload for `account.ads.initial_sync_completed` events. Fired once per ads-enabled account when the initial discovery + 90-day ad backfill finishes (whether it succeeded fully, partially, or failed). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadAccountAdsInitialSyncCompletedAccount**](WebhookPayloadAccountAdsInitialSyncCompletedAccount.md) |  |  |
|**sync** | [**WebhookPayloadAccountAdsInitialSyncCompletedSync**](WebhookPayloadAccountAdsInitialSyncCompletedSync.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| ACCOUNT_ADS_INITIAL_SYNC_COMPLETED | &quot;account.ads.initial_sync_completed&quot; |



