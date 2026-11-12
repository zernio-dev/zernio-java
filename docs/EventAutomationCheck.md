

# EventAutomationCheck

One event that reached an event automation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**automationId** | **String** |  |  |
|**checkedAt** | **OffsetDateTime** |  |  |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) | &#x60;paused&#x60;: the team used its free automation runs with no payment method on file, so the check did not run. &#x60;error&#x60; says why. |  |
|**evaluated** | **Integer** |  |  |
|**event** | **String** |  |  |
|**eventId** | **String** |  |  |
|**subject** | [**EventAutomationCheckSubject**](EventAutomationCheckSubject.md) |  |  |
|**facts** | **Map&lt;String, Object&gt;** | The event&#39;s facts as the trigger read them, keyed by fact name. Recorded only for an automation with no steps (one that only records each event).  Null for an automation with steps, whose filter results show the facts it compared, and on checks recorded before facts were kept. Content facts are null for a team that keeps no content. |  |
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
| PAUSED | &quot;paused&quot; |



