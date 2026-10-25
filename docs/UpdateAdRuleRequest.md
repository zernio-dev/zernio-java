

# UpdateAdRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**level** | **AdRuleLevel** |  |  [optional] |
|**campaignIds** | **List&lt;String&gt;** |  |  [optional] |
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  [optional] |
|**actions** | [**List&lt;AdRuleAction&gt;**](AdRuleAction.md) | Each type at most once, and at most one of &#x60;pause&#x60;, &#x60;activate&#x60; and &#x60;adjust_budget&#x60;. |  [optional] |
|**schedule** | [**AdRuleSchedule**](AdRuleSchedule.md) |  |  [optional] |
|**cooldownMinutes** | **Integer** |  |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |



