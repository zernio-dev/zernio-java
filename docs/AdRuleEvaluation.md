

# AdRuleEvaluation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**evaluatedAt** | **OffsetDateTime** |  |  |
|**today** | **LocalDate** | The ad account&#39;s calendar date the windows were resolved against. |  |
|**timezone** | **String** | IANA timezone of the ad account. |  |
|**timezoneAssumed** | **Boolean** | True when the ad account has no known timezone and UTC was assumed. |  |
|**currency** | **String** |  |  |
|**hourlyThrough** | **OffsetDateTime** | Where the hourly windows (&#x60;last_complete_hour&#x60;, &#x60;last_3h&#x60;, &#x60;today_so_far&#x60;) ended: the end of the latest hour a sync has settled. Null when the rule has none or they could not be read. |  [optional] |
|**matched** | **Integer** | How many objects meet every condition. |  |
|**objects** | [**List&lt;AdRuleObjectEvaluation&gt;**](AdRuleObjectEvaluation.md) | Every delivering campaign or ad set in scope (for an &#x60;activate&#x60; rule, the rule-paused ones it may reactivate). |  |
|**groups** | [**List&lt;AdRuleEvaluationGroupsInner&gt;**](AdRuleEvaluationGroupsInner.md) | Each group&#39;s totals, for a rule with groups. Null otherwise. |  [optional] |



