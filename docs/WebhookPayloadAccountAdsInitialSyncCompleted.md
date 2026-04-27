

# WebhookPayloadAccountAdsInitialSyncCompleted

Webhook payload for `account.ads.initial_sync_completed` events. Fired once per ads-enabled account when the initial discovery + 90-day ad backfill finishes (whether it succeeded fully, partially, or failed). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadAccountAdsInitialSyncCompletedAccount**](WebhookPayloadAccountAdsInitialSyncCompletedAccount.md) |  |  |
|**sync** | [**WebhookPayloadAccountAdsInitialSyncCompletedSync**](WebhookPayloadAccountAdsInitialSyncCompletedSync.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| ACCOUNT_ADS_INITIAL_SYNC_COMPLETED | &quot;account.ads.initial_sync_completed&quot; |



