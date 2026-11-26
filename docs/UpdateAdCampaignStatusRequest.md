

# UpdateAdCampaignStatusRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**stage** | **Boolean** | Send true to stage this change instead of applying it. Nothing is written to the ad network; the response is &#x60;202&#x60; with the staged change and its diff. Apply it with POST /v1/ads/changes/{changeId}/confirm. Meta, Google, TikTok, X, Snapchat and Reddit; cannot be combined with &#x60;validateOnly&#x60; or &#x60;dryRun&#x60;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



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
| REDDIT | &quot;reddit&quot; |
| MICROSOFT | &quot;microsoft&quot; |
| AMAZON | &quot;amazon&quot; |
| TRADEDESK | &quot;tradedesk&quot; |
| SNAPCHAT | &quot;snapchat&quot; |



