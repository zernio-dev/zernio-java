

# UpdateAdCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id owning the ad account. Required only to update an EMPTY campaign (zero ads), which has no local Ad documents to resolve a token from. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**budget** | [**UpdateAdCampaignRequestBudget**](UpdateAdCampaignRequestBudget.md) |  |  [optional] |
|**bidStrategy** | **BidStrategy** | Campaign-level default. Ad sets inherit this unless they override. |  [optional] |
|**name** | **String** | Rename the campaign (Meta only; other platforms return 501). At least one of budget/bidStrategy/name/platformSpecificData is required. |  [optional] |
|**platformSpecificData** | [**UpdateAdCampaignRequestPlatformSpecificData**](UpdateAdCampaignRequestPlatformSpecificData.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |



