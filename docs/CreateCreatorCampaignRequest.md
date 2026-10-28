

# CreateCreatorCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Profile the campaign lives in. Creator accounts connect into the same workspace. |  |
|**name** | **String** |  |  |
|**brandName** | **String** |  |  |
|**economics** | [**CreatorCampaignEconomics**](CreatorCampaignEconomics.md) |  |  |
|**caps** | [**CreatorCampaignCaps**](CreatorCampaignCaps.md) | Omitted, the campaign starts with authenticityThreshold 40 and no other caps. |  [optional] |
|**platforms** | [**List&lt;PlatformsEnum&gt;**](#List&lt;PlatformsEnum&gt;) | Platforms creators may post on. At least one is needed to activate. |  [optional] |
|**contentRules** | **String** |  |  [optional] |
|**startsAt** | **OffsetDateTime** |  |  [optional] |
|**endsAt** | **OffsetDateTime** |  |  [optional] |
|**trackingDays** | **Integer** |  |  [optional] |
|**holdDays** | **Integer** |  |  [optional] |
|**maxPostAgeMinutes** | **Integer** |  |  [optional] |
|**settlement** | [**SettlementEnum**](#SettlementEnum) |  |  [optional] |
|**branding** | [**CreatorCampaignBranding**](CreatorCampaignBranding.md) |  |  [optional] |



## Enum: List&lt;PlatformsEnum&gt;

| Name | Value |
|---- | -----|
| TIKTOK | &quot;tiktok&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| YOUTUBE | &quot;youtube&quot; |



## Enum: SettlementEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| EXTERNAL | &quot;external&quot; |
| TREASURY | &quot;treasury&quot; |



