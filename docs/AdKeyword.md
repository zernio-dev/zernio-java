

# AdKeyword


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Zernio keyword ID. Accepted as &#x60;keywordId&#x60; by PATCH/DELETE /v1/ads/keywords/{keywordId}. |  [optional] |
|**platformCriterionId** | **String** | Google ad_group_criterion.criterion_id. Unique only within its ad group (&#x60;adSetId&#x60;), not across the account. |  [optional] |
|**resourceName** | **String** | Google resource name, customers/{adAccountId}/adGroupCriteria/{adSetId}~{platformCriterionId}. |  [optional] |
|**accountId** | **String** | Account ID owning the sync |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**adAccountId** | **String** | Google customer ID |  [optional] |
|**campaignId** | **String** |  |  [optional] |
|**campaignName** | **String** |  |  [optional] |
|**campaignStatus** | **String** |  |  [optional] |
|**adSetId** | **String** | Google ad group ID |  [optional] |
|**adSetName** | **String** |  |  [optional] |
|**adSetStatus** | **String** |  |  [optional] |
|**keyword** | **String** |  |  [optional] |
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**negative** | **Boolean** |  |  [optional] |
|**qualityScore** | **Integer** | Deprecated, use &#x60;quality.score&#x60;. Google Quality Score, 1-10. Null when unrated. |  [optional] |
|**quality** | [**AdKeywordQuality**](AdKeywordQuality.md) |  |  [optional] |
|**syncedAt** | **OffsetDateTime** |  |  [optional] |
|**metrics** | [**AdKeywordMetrics**](AdKeywordMetrics.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |



## Enum: MatchTypeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;exact&quot; |
| PHRASE | &quot;phrase&quot; |
| BROAD | &quot;broad&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



