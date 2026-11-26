

# AutomationRunDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**automationId** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;live&#x60; while it runs or waits (a comment to DM run waiting for its follow gate is live). |  |
|**subject** | [**AutomationRunSubject**](AutomationRunSubject.md) |  |  |
|**startedAt** | **OffsetDateTime** |  |  |
|**endedAt** | **OffsetDateTime** |  |  |
|**exitReason** | **String** | Why an exited or failed run stopped, for example &#x60;handoff&#x60; (a flow handed the conversation to a person), &#x60;wait_expired&#x60;, &#x60;superseded&#x60;, &#x60;replied&#x60;, &#x60;unsubscribed&#x60; or &#x60;skipped&#x60;. |  |
|**error** | **String** |  |  |
|**steps** | [**AutomationRunSteps**](AutomationRunSteps.md) |  |  |
|**trace** | [**List&lt;AutomationRunDetailAllOfTrace&gt;**](AutomationRunDetailAllOfTrace.md) | Each step in order. Null where the run&#39;s store keeps no step by step record (runs on the automation engine keep where they are and how many steps they took). |  |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| AD_RULE | &quot;ad_rule&quot; |
| EVENT | &quot;event&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| SEQUENCE | &quot;sequence&quot; |
| COMMENT | &quot;comment&quot; |
| WORKFLOW | &quot;workflow&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| LIVE | &quot;live&quot; |
| PAUSED | &quot;paused&quot; |
| COMPLETED | &quot;completed&quot; |
| EXITED | &quot;exited&quot; |
| FAILED | &quot;failed&quot; |



