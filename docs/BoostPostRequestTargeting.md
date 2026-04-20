

# BoostPostRequestTargeting


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ageMin** | **Integer** |  |  [optional] |
|**ageMax** | **Integer** |  |  [optional] |
|**countries** | **List&lt;String&gt;** |  |  [optional] |
|**interests** | [**List&lt;UpdateAdRequestTargetingInterestsInner&gt;**](UpdateAdRequestTargetingInterestsInner.md) | Interest objects from /v1/ads/interests. Each must include id and name. |  [optional] |
|**advantageAudience** | [**AdvantageAudienceEnum**](#AdvantageAudienceEnum) | Meta only. 0 &#x3D; disabled (default), 1 &#x3D; enabled. |  [optional] |



## Enum: AdvantageAudienceEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



