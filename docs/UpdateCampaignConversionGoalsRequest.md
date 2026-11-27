

# UpdateCampaignConversionGoalsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**goals** | [**List&lt;GoogleBiddableGoalInput&gt;**](GoogleBiddableGoalInput.md) |  |  [optional] |
|**goalConfigLevel** | [**GoalConfigLevelEnum**](#GoalConfigLevelEnum) |  |  [optional] |
|**customConversionGoalId** | **String** | Custom goal to bid on, or null to clear |  [optional] |



## Enum: GoalConfigLevelEnum

| Name | Value |
|---- | -----|
| CUSTOMER | &quot;CUSTOMER&quot; |
| CAMPAIGN | &quot;CAMPAIGN&quot; |



