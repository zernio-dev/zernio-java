

# DeleteAdCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**accountId** | **String** | Zernio SocialAccount id owning the ad account. Required only to delete an EMPTY campaign (zero ads), which has no local Ad documents to resolve a token from. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| GOOGLE | &quot;google&quot; |



