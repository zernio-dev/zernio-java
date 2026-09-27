

# GetCampaignConversionGoals200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignId** | **String** |  |  [optional] |
|**goalConfigLevel** | [**GoalConfigLevelEnum**](#GoalConfigLevelEnum) |  |  [optional] |
|**customConversionGoalId** | **String** |  |  [optional] |
|**goals** | [**List&lt;GoogleCampaignConversionGoalsGoalsInner&gt;**](GoogleCampaignConversionGoalsGoalsInner.md) |  |  [optional] |
|**customerId** | **String** |  |  [optional] |
|**cachedAt** | **OffsetDateTime** |  |  [optional] |
|**stale** | **Boolean** |  |  [optional] |



## Enum: GoalConfigLevelEnum

| Name | Value |
|---- | -----|
| CUSTOMER | &quot;CUSTOMER&quot; |
| CAMPAIGN | &quot;CAMPAIGN&quot; |
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



