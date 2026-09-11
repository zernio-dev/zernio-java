

# CreateStandaloneAd200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**node** | [**NodeEnum**](#NodeEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**reason** | **String** | Why the node could not be validated (on skipped), or what the dry run could not check and what the request would do as sent (on validated). A Performance Max validation with no location targeting reports here that the campaign would run worldwide. |  [optional] |



## Enum: NodeEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| AD_SET | &quot;adSet&quot; |
| CREATIVE | &quot;creative&quot; |
| AD | &quot;ad&quot; |
| PERFORMANCE_MAX_CAMPAIGN | &quot;performanceMaxCampaign&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VALIDATED | &quot;validated&quot; |
| SKIPPED | &quot;skipped&quot; |



