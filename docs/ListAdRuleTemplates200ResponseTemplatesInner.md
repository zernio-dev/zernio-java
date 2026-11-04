

# ListAdRuleTemplates200ResponseTemplatesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  |
|**level** | **AdRuleLevel** |  |  |
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  |
|**actions** | [**List&lt;AdRuleAction&gt;**](AdRuleAction.md) | Each type at most once, and at most one of &#x60;pause&#x60;, &#x60;activate&#x60;, &#x60;adjust_budget&#x60;, &#x60;duplicate&#x60; and &#x60;edit_name&#x60;. |  |
|**goal** | [**GoalEnum**](#GoalEnum) | What the template is for: stop waste, grow what works, act at set times, or only tell you. |  |
|**schedule** | [**AdRuleSchedule**](AdRuleSchedule.md) |  |  |
|**cooldownMinutes** | **Integer** |  |  |
|**platforms** | **List&lt;String&gt;** |  |  |



## Enum: GoalEnum

| Name | Value |
|---- | -----|
| PROTECT | &quot;protect&quot; |
| SCALE | &quot;scale&quot; |
| SCHEDULE | &quot;schedule&quot; |
| ALERT | &quot;alert&quot; |



