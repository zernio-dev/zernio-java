

# EventAutomationCheck

One event that reached an event automation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**automationId** | **String** |  |  |
|**checkedAt** | **OffsetDateTime** |  |  |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) |  |  |
|**evaluated** | **Integer** |  |  |
|**event** | **String** |  |  |
|**eventId** | **String** |  |  |
|**subject** | [**EventAutomationCheckSubject**](EventAutomationCheckSubject.md) |  |  |
|**filter** | [**List&lt;AutomationFactResult&gt;**](AutomationFactResult.md) |  |  |
|**actions** | [**List&lt;AutomationRunResult&gt;**](AutomationRunResult.md) |  |  |
|**error** | **String** |  |  |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| TRIGGERED | &quot;triggered&quot; |
| NO_MATCH | &quot;no_match&quot; |
| COOLDOWN | &quot;cooldown&quot; |
| DAILY_LIMIT | &quot;daily_limit&quot; |
| FAILED | &quot;failed&quot; |



