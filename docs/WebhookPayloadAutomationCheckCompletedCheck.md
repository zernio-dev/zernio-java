

# WebhookPayloadAutomationCheckCompletedCheck


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**slot** | **OffsetDateTime** | The scheduled time the check ran for. |  |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) | &#x60;paused&#x60;: the team used its free automation runs with no payment method on file, so the check did not run. &#x60;error&#x60; says why. |  |
|**subjectsEvaluated** | **Integer** | How many objects the check read. |  |
|**actionsCount** | **Integer** | How many actions it recorded. |  |
|**error** | **String** |  |  |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| TRIGGERED | &quot;triggered&quot; |
| NO_MATCH | &quot;no_match&quot; |
| COOLDOWN | &quot;cooldown&quot; |
| DAILY_LIMIT | &quot;daily_limit&quot; |
| FAILED | &quot;failed&quot; |
| PAUSED | &quot;paused&quot; |



