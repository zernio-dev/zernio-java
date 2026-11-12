

# AdRuleRunEvaluation

The matched objects with their condition values, and what each action did.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rule** | [**AdRuleRunEvaluationRule**](AdRuleRunEvaluationRule.md) |  |  [optional] |
|**today** | **LocalDate** |  |  [optional] |
|**timezone** | **String** |  |  [optional] |
|**timezoneAssumed** | **Boolean** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**hourlyThrough** | **OffsetDateTime** | Where the run&#39;s hourly windows ended. Absent on runs recorded before November 2026. |  [optional] |
|**matched** | [**List&lt;AdRuleObjectEvaluation&gt;**](AdRuleObjectEvaluation.md) |  |  [optional] |
|**actions** | [**List&lt;AdRuleRunEvaluationActionsInner&gt;**](AdRuleRunEvaluationActionsInner.md) |  |  [optional] |
|**notification** | [**AdRuleRunEvaluationNotification**](AdRuleRunEvaluationNotification.md) |  |  [optional] |



