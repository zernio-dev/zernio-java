

# BulkUpdateAdCampaignStatusRequestCampaignsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformCampaignId** | **String** | The campaign id on the ad platform (e.g. the numeric Google campaign id), not a Zernio id. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) | The ad platform, e.g. &#x60;google&#x60; for Google Ads. The ads connection slug (&#x60;googleads&#x60;, &#x60;tiktokads&#x60;, ...) is accepted as an alias. &#x60;metaads&#x60; is not: send &#x60;facebook&#x60; or &#x60;instagram&#x60;. |  |



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
| GOOGLEADS | &quot;googleads&quot; |
| TIKTOKADS | &quot;tiktokads&quot; |
| LINKEDINADS | &quot;linkedinads&quot; |
| PINTERESTADS | &quot;pinterestads&quot; |
| XADS | &quot;xads&quot; |
| OPENAIADS | &quot;openaiads&quot; |



