

# CreateAdSetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id owning the Google Ads connection. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Only \&quot;google\&quot; is implemented today; every other value returns 501. |  |
|**campaignId** | **String** | Google platform campaign ID (numeric) the ad group is created under. |  |
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**maxCpc** | **BigDecimal** | Max CPC of the new ad group, in the account&#39;s currency units. Send it when the campaign uses Manual CPC: Google gives an ad group without one a 0.01 bid. |  [optional] |
|**adAccountId** | **String** | Platform ad account ID (Google customer ID, digits only). Only required when the connection has more than one. |  [optional] |
|**customerId** | **String** | Alias of adAccountId, kept for existing callers |  [optional] |



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



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PAUSED | &quot;PAUSED&quot; |



