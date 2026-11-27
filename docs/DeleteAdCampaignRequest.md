

# DeleteAdCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**accountId** | **String** | Zernio SocialAccount id owning the ad account. Required only to delete an EMPTY campaign (zero ads), which has no local Ad documents to resolve a token from. |  [optional] |
|**adAccountId** | **String** | X only, for an EMPTY campaign that was never synced: the X ad account id the campaign belongs to (lowercase letters and digits). The synced campaign&#39;s ad account wins when there is one. Also accepted on the query string. |  [optional] |



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



