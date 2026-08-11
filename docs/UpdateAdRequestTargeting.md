

# UpdateAdRequestTargeting

Meta + TikTok (demographics/interests) and Google (keyword edits only). Pinterest / X / LinkedIn return 501. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keywords** | [**List&lt;UpdateAdRequestTargetingKeywordsInner&gt;**](UpdateAdRequestTargetingKeywordsInner.md) | Google only. The FULL new set of positive keywords for the ad group; live keywords not listed are removed. Entries are strings (BROAD) or { text, matchType } with matchType exact | phrase | broad. Mirrored to GET /v1/ads/keywords immediately. |  [optional] |
|**negativeKeywords** | [**List&lt;UpdateAdRequestTargetingKeywordsInner&gt;**](UpdateAdRequestTargetingKeywordsInner.md) | Google only. Same declarative contract as keywords, for the ad group&#39;s negative keywords. |  [optional] |
|**ageMin** | **Integer** |  |  [optional] |
|**ageMax** | **Integer** |  |  [optional] |
|**countries** | **List&lt;String&gt;** |  |  [optional] |
|**interests** | [**List&lt;UpdateAdRequestTargetingInterestsInner&gt;**](UpdateAdRequestTargetingInterestsInner.md) | Interest objects from /v1/ads/interests. Each must include id and name. |  [optional] |
|**advantageAudience** | [**AdvantageAudienceEnum**](#AdvantageAudienceEnum) | Meta only. Omit to preserve the existing setting on update. 0 &#x3D; disabled, 1 &#x3D; enabled. |  [optional] |



## Enum: AdvantageAudienceEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



