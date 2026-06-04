

# UpdateAdCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**budget** | [**UpdateAdCampaignRequestBudget**](UpdateAdCampaignRequestBudget.md) |  |  [optional] |
|**bidStrategy** | **BidStrategy** | Campaign-level default. Ad sets inherit this unless they override. |  [optional] |
|**name** | **String** | Rename the campaign (Meta only; other platforms return 501). At least one of budget/bidStrategy/name is required. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |



