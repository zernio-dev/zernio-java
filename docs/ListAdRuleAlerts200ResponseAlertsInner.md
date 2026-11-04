

# ListAdRuleAlerts200ResponseAlertsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**objectId** | **String** | Platform campaign, ad set or ad ID. |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  |
|**consecutiveMatches** | **Integer** |  |  |
|**openedAt** | **OffsetDateTime** |  |  |
|**lastMatchedAt** | **OffsetDateTime** |  |  |
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



