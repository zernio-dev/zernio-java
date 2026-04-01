

# AdCampaign


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformCampaignId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**campaignName** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Derived from child ad statuses |  [optional] |
|**adCount** | **Integer** |  |  [optional] |
|**budget** | [**AdBudget**](AdBudget.md) |  |  [optional] |
|**metrics** | [**AdMetrics**](AdMetrics.md) |  |  [optional] |
|**platformAdAccountId** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**earliestAd** | **OffsetDateTime** |  |  [optional] |
|**latestAd** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| TIKTOK | &quot;tiktok&quot; |
| LINKEDIN | &quot;linkedin&quot; |
| PINTEREST | &quot;pinterest&quot; |
| GOOGLE | &quot;google&quot; |
| TWITTER | &quot;twitter&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |
| PENDING_REVIEW | &quot;pending_review&quot; |
| REJECTED | &quot;rejected&quot; |
| COMPLETED | &quot;completed&quot; |
| CANCELLED | &quot;cancelled&quot; |
| ERROR | &quot;error&quot; |



