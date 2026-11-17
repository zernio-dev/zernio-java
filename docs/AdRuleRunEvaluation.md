

# AdRuleRunEvaluation

The matched objects with their condition values, and what each action did. Null on a run that matched nothing, unless some objects could not be read.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**unreadObjects** | **Integer** | On a run that matched nothing: how many objects had a condition whose value could not be read, so they could not match. A campaign with under 3 of the 4 previous weeks of data has no &#x60;usual&#x60; yet. |  [optional] |
|**rule** | [**AdRuleRunEvaluationRule**](AdRuleRunEvaluationRule.md) |  |  [optional] |
|**today** | **LocalDate** |  |  [optional] |
|**timezone** | **String** |  |  [optional] |
|**timezoneAssumed** | **Boolean** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**hourlyThrough** | **OffsetDateTime** | Where the run&#39;s hourly windows ended. Absent on runs recorded before November 2026. |  [optional] |
|**matched** | [**List&lt;AdRuleObjectEvaluation&gt;**](AdRuleObjectEvaluation.md) | The matched objects, at most 200. &#x60;matchedTotal&#x60; has the full count. |  [optional] |
|**matchedTotal** | **Integer** | How many objects matched, including those past the 200 recorded. Absent on runs recorded before November 2026. |  [optional] |
|**actions** | [**List&lt;AdRuleRunEvaluationActionsInner&gt;**](AdRuleRunEvaluationActionsInner.md) |  |  [optional] |
|**notification** | [**AdRuleRunEvaluationNotification**](AdRuleRunEvaluationNotification.md) |  |  [optional] |



