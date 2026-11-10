

# LaunchCampaignAdsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**submissionIds** | **List&lt;String&gt;** | Approved submissions to run as ads. |  |
|**network** | [**NetworkEnum**](#NetworkEnum) | Meta runs Instagram and Facebook posts; TikTok runs TikTok posts. |  |
|**accountId** | **String** | The brand&#39;s connected ads account (Facebook or TikTok) the ads run from, as in &#x60;/v1/accounts&#x60;. |  |
|**adAccountId** | **String** | Platform ad account ID. |  |
|**adSetId** | **String** | Existing Meta ad set the ads go into. Required when &#x60;network&#x60; is &#x60;meta&#x60;. |  [optional] |
|**existingCampaignId** | **String** | Existing TikTok campaign that gets one ad group per post. Required when &#x60;network&#x60; is &#x60;tiktok&#x60;. |  [optional] |
|**dailyBudget** | **BigDecimal** | Daily budget of each TikTok ad group, in the ad account currency. Required when &#x60;network&#x60; is &#x60;tiktok&#x60;. |  [optional] |
|**identity** | [**IdentityEnum**](#IdentityEnum) | Whose handle the ad runs under. TikTok takes &#x60;creator&#x60; only. |  |
|**body** | **String** | Primary text of brand ads. Defaults to the post caption. |  [optional] |
|**headline** | **String** |  |  [optional] |
|**callToAction** | **String** | Call to action, as in &#x60;POST /v1/ads/create&#x60;. |  [optional] |
|**linkUrl** | **URI** | Destination URL (http or https). |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Ads launch paused unless set to &#x60;ACTIVE&#x60;. |  [optional] |



## Enum: NetworkEnum

| Name | Value |
|---- | -----|
| META | &quot;meta&quot; |
| TIKTOK | &quot;tiktok&quot; |



## Enum: IdentityEnum

| Name | Value |
|---- | -----|
| BRAND | &quot;brand&quot; |
| CREATOR | &quot;creator&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PAUSED | &quot;PAUSED&quot; |



