

# LaunchCampaignAds200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**submissionId** | **String** |  |  |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) | &#x60;in_progress&#x60;: another launch of this post into the same placement is still running. |  |
|**identity** | [**IdentityEnum**](#IdentityEnum) |  |  |
|**adId** | **String** | Zernio ad id, as in /v1/ads. |  |
|**error** | **String** | Why the post did not launch. |  |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| LAUNCHED | &quot;launched&quot; |
| ALREADY_LAUNCHED | &quot;already_launched&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |
| FAILED | &quot;failed&quot; |



## Enum: IdentityEnum

| Name | Value |
|---- | -----|
| BRAND | &quot;brand&quot; |
| CREATOR | &quot;creator&quot; |



