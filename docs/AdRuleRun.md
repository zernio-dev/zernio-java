

# AdRuleRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**ranAt** | **OffsetDateTime** |  |  |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) | Result of the rule run:  - &#x60;triggered&#x60;: the rule acted on at least one object (&#x60;error&#x60; is set if the webhook could not be sent afterwards). - &#x60;cooldown&#x60;: objects matched but all were in cooldown. - &#x60;daily_limit&#x60;: objects matched but the rule had used its &#x60;maxChangesPerDay&#x60;. - &#x60;paused&#x60;: the run did not happen: the team used its free automation runs with no payment method on file (see &#x60;error&#x60;). - &#x60;no_match&#x60;: nothing matched. - &#x60;failed&#x60;: the metrics could not be read, every action failed, or the webhook of a notify-only rule could not be sent (see &#x60;error&#x60;).  |  |
|**objectsEvaluated** | **Integer** | Objects the rule judged. 0 means its campaigns and filters matched nothing that is running. |  |
|**actedObjectIds** | **List&lt;String&gt;** |  |  |
|**evaluation** | [**AdRuleRunEvaluation**](AdRuleRunEvaluation.md) |  |  |
|**error** | **String** |  |  |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| TRIGGERED | &quot;triggered&quot; |
| COOLDOWN | &quot;cooldown&quot; |
| DAILY_LIMIT | &quot;daily_limit&quot; |
| NO_MATCH | &quot;no_match&quot; |
| FAILED | &quot;failed&quot; |
| PAUSED | &quot;paused&quot; |



