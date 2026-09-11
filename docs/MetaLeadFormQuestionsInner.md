

# MetaLeadFormQuestionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**key** | **String** |  |  [optional] |
|**label** | **String** |  |  [optional] |
|**type** | **String** | EMAIL, PHONE, FULL_NAME, CUSTOM, ... |  [optional] |
|**inlineContext** | **String** |  |  [optional] |
|**options** | [**List&lt;BoostPostRequestTrackingUrlTagsInner&gt;**](BoostPostRequestTrackingUrlTagsInner.md) |  |  [optional] |
|**conditionalQuestionsGroupId** | **String** | READ-ONLY. Conditional logic can only be authored in Meta form builder; Meta has no create parameter for it. |  [optional] |
|**conditionalQuestionsChoices** | **List&lt;Object&gt;** | READ-ONLY. Which answers reveal the conditional group. |  [optional] |
|**dependentConditionalQuestions** | **List&lt;Object&gt;** | READ-ONLY. Questions revealed by the conditional group. |  [optional] |



