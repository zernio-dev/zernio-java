

# AdRuleRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**ranAt** | **OffsetDateTime** |  |  |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) | &#x60;triggered&#x60;: the rule acted on at least one object (&#x60;error&#x60; is set if the webhook could not be sent afterwards). &#x60;cooldown&#x60;: objects matched but all were in cooldown. &#x60;no_match&#x60;: nothing matched. &#x60;failed&#x60;: the metrics could not be read, every action failed, or the webhook of a notify-only rule could not be sent (see &#x60;error&#x60;). |  |
|**objectsEvaluated** | **Integer** |  |  |
|**actedObjectIds** | **List&lt;String&gt;** |  |  |
|**evaluation** | [**AdRuleRunEvaluation**](AdRuleRunEvaluation.md) |  |  |
|**error** | **String** |  |  |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| TRIGGERED | &quot;triggered&quot; |
| COOLDOWN | &quot;cooldown&quot; |
| NO_MATCH | &quot;no_match&quot; |
| FAILED | &quot;failed&quot; |



