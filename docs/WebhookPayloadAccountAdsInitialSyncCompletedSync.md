

# WebhookPayloadAccountAdsInitialSyncCompletedSync

Summary of the initial ads sync backfill results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | Overall outcome of the initial sync. |  |
|**totalAds** | **Integer** | Total number of ads discovered for backfill. |  |
|**synced** | **Integer** | Number of ads successfully synced. |  |
|**failed** | **Integer** | Number of ads that failed to sync. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILURE | &quot;failure&quot; |



