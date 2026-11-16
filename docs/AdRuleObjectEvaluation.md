

# AdRuleObjectEvaluation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform ID of the campaign or ad set. |  |
|**name** | **String** |  |  |
|**campaignId** | **String** |  |  |
|**matched** | **Boolean** | True when every condition holds. |  |
|**group** | **String** | For a rule with groups: the group this campaign was judged in. &#x60;matched&#x60; and &#x60;conditions&#x60; are the group&#39;s. |  [optional] |
|**conditions** | [**List&lt;AdRuleObjectEvaluationConditionsInner&gt;**](AdRuleObjectEvaluationConditionsInner.md) |  |  |
|**readings** | [**List&lt;AdRuleObjectEvaluationReadingsInner&gt;**](AdRuleObjectEvaluationReadingsInner.md) | On a matched object: spend, impressions and clicks over each window its conditions read, and the other search impression shares when a condition reads one. Left out where a condition already reads the value. |  [optional] |



