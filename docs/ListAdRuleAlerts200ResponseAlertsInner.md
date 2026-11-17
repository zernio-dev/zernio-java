

# ListAdRuleAlerts200ResponseAlertsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**objectId** | **String** | Platform campaign, ad set or ad ID, or the id of the keyword or search term. |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  |
|**consecutiveMatches** | **Integer** |  |  |
|**openedAt** | **OffsetDateTime** |  |  |
|**lastMatchedAt** | **OffsetDateTime** |  |  |
|**lastEvaluatedAt** | **OffsetDateTime** | When a run last evaluated the object of this alert. Older than the latest run means that run did not evaluate it. |  |
|**resolvedAt** | **OffsetDateTime** |  |  |
|**resolvedReason** | [**ResolvedReasonEnum**](#ResolvedReasonEnum) |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| OPEN | &quot;open&quot; |
| RESOLVED | &quot;resolved&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| WARNING | &quot;warning&quot; |
| CRITICAL | &quot;critical&quot; |



## Enum: ResolvedReasonEnum

| Name | Value |
|---- | -----|
| CONDITION_CLEARED | &quot;condition_cleared&quot; |
| ACTION_APPLIED | &quot;action_applied&quot; |
| NOT_EVALUATED | &quot;not_evaluated&quot; |
| AUTOMATION_CHANGED | &quot;automation_changed&quot; |
| AUTOMATION_OFF | &quot;automation_off&quot; |



