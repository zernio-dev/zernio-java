

# CreateStandaloneAd200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**node** | [**NodeEnum**](#NodeEnum) | &#x60;identity&#x60; is TikTok only: the identity the ad would run as. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**reason** | **String** | Explanation for the node&#39;s result:  - On skipped: why the node could not be validated. - On unverified: why the platform could not dry-run it although the other nodes passed (Meta), or what only a real create checks (TikTok). - On validated: what the dry run could not check, and what the request would do as sent. For example, a Performance Max validation with no location targeting reports here that the campaign would run worldwide. |  [optional] |



## Enum: NodeEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| AD_SET | &quot;adSet&quot; |
| CREATIVE | &quot;creative&quot; |
| AD | &quot;ad&quot; |
| PERFORMANCE_MAX_CAMPAIGN | &quot;performanceMaxCampaign&quot; |
| IDENTITY | &quot;identity&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VALIDATED | &quot;validated&quot; |
| SKIPPED | &quot;skipped&quot; |
| UNVERIFIED | &quot;unverified&quot; |



