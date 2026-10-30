

# AdsAlert


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable for the same problem on the same entity. Pass it to POST /v1/ads/alerts/{alertId}/dismiss. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) |  |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**message** | **String** | What happened, in plain words. For a rejection or delivery issue, the platform&#39;s own reason when it gave one. |  [optional] |
|**platform** | **String** |  |  [optional] |
|**platformAdAccountId** | **String** |  |  [optional] |
|**entity** | [**AdsAlertEntity**](AdsAlertEntity.md) |  |  [optional] |
|**adId** | **String** | The Zernio ad id when the entity is an ad, for GET /v1/ads/{adId}. |  [optional] |
|**accountId** | **String** | The Zernio ads connection, on connection_lost and sync_failing alerts. |  [optional] |
|**currency** | **String** |  |  [optional] |
|**detectedAt** | **OffsetDateTime** |  |  [optional] |
|**fix** | [**AdsAlertFix**](AdsAlertFix.md) |  |  [optional] |
|**dismissed** | **Boolean** |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| AD_REJECTED | &quot;ad_rejected&quot; |
| DELIVERY_ISSUE | &quot;delivery_issue&quot; |
| PAYMENT | &quot;payment&quot; |
| BUDGET_LIMITED | &quot;budget_limited&quot; |
| SPEND_NO_RESULTS | &quot;spend_no_results&quot; |
| CONNECTION_LOST | &quot;connection_lost&quot; |
| SYNC_FAILING | &quot;sync_failing&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;error&quot; |
| WARNING | &quot;warning&quot; |
| INFO | &quot;info&quot; |



