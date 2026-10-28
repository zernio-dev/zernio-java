

# CreateAdSetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id owning the Google Ads or Reddit Ads connection. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) | \&quot;google\&quot; and \&quot;reddit\&quot; are implemented; every other value returns 501. |  |
|**campaignId** | **String** | Platform campaign ID the ad group is created under (numeric on Google). |  |
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**maxCpc** | **BigDecimal** | Max CPC of the new ad group, in the account&#39;s currency units. Send it when the campaign uses Manual CPC: Google gives an ad group without one a 0.01 bid. |  [optional] |
|**adAccountId** | **String** | Platform ad account ID: the Google customer ID (digits only, only required when the connection has more than one) or the Reddit ad account id (required). |  [optional] |
|**customerId** | **String** | Google only. Alias of adAccountId, kept for existing callers |  [optional] |
|**budgetAmount** | **BigDecimal** | Reddit only. Budget of the new ad group, in the ad account&#39;s currency units. Required when the campaign has no campaign budget; 400 under campaign budget optimization, where the campaign budget funds the ad group. |  [optional] |
|**budgetType** | [**BudgetTypeEnum**](#BudgetTypeEnum) | Reddit only. Sent together with budgetAmount. |  [optional] |
|**startDate** | **String** | Reddit only. ISO 8601 start of the ad group. Defaults to now, or to the campaign start when it is in the future. |  [optional] |
|**endDate** | **String** | Reddit only. ISO 8601 end of the ad group. Defaults to the campaign end. |  [optional] |
|**targeting** | [**TargetingSpec**](TargetingSpec.md) |  |  [optional] |
|**promotedObject** | [**CreateAdSetRequestPromotedObject**](CreateAdSetRequestPromotedObject.md) |  |  [optional] |
|**optimizationGoal** | **String** | Reddit only. VIDEO_VIEW_6S (default) or VIDEO_VIEW_15S on a video views campaign. |  [optional] |
|**bidStrategy** | [**BidStrategyEnum**](#BidStrategyEnum) | Reddit only. Defaults to LOWEST_COST_WITHOUT_CAP. Not accepted under campaign budget optimization. |  [optional] |
|**bidAmount** | **BigDecimal** | Reddit only. Bid cap in currency units, sent with bidStrategy. |  [optional] |



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
| OPENAI | &quot;openai&quot; |
| REDDIT | &quot;reddit&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PAUSED | &quot;PAUSED&quot; |



## Enum: BudgetTypeEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| LIFETIME | &quot;lifetime&quot; |



## Enum: BidStrategyEnum

| Name | Value |
|---- | -----|
| LOWEST_COST_WITHOUT_CAP | &quot;LOWEST_COST_WITHOUT_CAP&quot; |
| LOWEST_COST_WITH_BID_CAP | &quot;LOWEST_COST_WITH_BID_CAP&quot; |
| COST_CAP | &quot;COST_CAP&quot; |



