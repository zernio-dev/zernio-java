

# WebhookPayloadAutomationCheckCompletedCheck


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**slot** | **OffsetDateTime** | The scheduled time the check ran for. |  |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) |  |  |
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



