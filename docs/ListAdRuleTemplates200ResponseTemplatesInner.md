

# ListAdRuleTemplates200ResponseTemplatesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  |
|**level** | **AdRuleLevel** |  |  |
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  |
|**actions** | [**List&lt;AdRuleAction&gt;**](AdRuleAction.md) | Each type at most once, and at most one of &#x60;pause&#x60;, &#x60;activate&#x60; and &#x60;adjust_budget&#x60;. |  |
|**schedule** | [**AdRuleSchedule**](AdRuleSchedule.md) |  |  |
|**cooldownMinutes** | **Integer** |  |  |
|**platforms** | **List&lt;String&gt;** |  |  |



