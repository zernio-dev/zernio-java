

# UpdateCreatorCampaignRequest

Every field is optional; send at least one. `economics` can only change while the campaign is a draft.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**brandName** | **String** |  |  [optional] |
|**platforms** | [**List&lt;PlatformsEnum&gt;**](#List&lt;PlatformsEnum&gt;) |  |  [optional] |
|**contentRules** | **String** |  |  [optional] |
|**startsAt** | **OffsetDateTime** |  |  [optional] |
|**endsAt** | **OffsetDateTime** |  |  [optional] |
|**trackingDays** | **Integer** |  |  [optional] |
|**holdDays** | **Integer** |  |  [optional] |
|**maxPostAgeMinutes** | **Integer** |  |  [optional] |
|**settlement** | [**SettlementEnum**](#SettlementEnum) |  |  [optional] |
|**economics** | [**CreatorCampaignEconomics**](CreatorCampaignEconomics.md) |  |  [optional] |
|**caps** | [**CreatorCampaignCaps**](CreatorCampaignCaps.md) |  |  [optional] |
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



