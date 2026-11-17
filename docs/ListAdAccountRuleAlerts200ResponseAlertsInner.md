

# ListAdAccountRuleAlerts200ResponseAlertsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ruleId** | **String** | The rule the alert belongs to. |  |
|**id** | **String** |  |  |
|**objectId** | **String** | Platform campaign, ad set or ad ID, or the id of the keyword or search term. |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  |
|**consecutiveMatches** | **Integer** |  |  |
|**openedAt** | **OffsetDateTime** |  |  |
|**lastMatchedAt** | **OffsetDateTime** |  |  |
|**lastEvaluatedAt** | **OffsetDateTime** | When a run last evaluated the object of this alert. Older than the latest run of its rule means that run did not evaluate it. |  |
|**resolvedAt** | **OffsetDateTime** | Always null here: only open alerts are listed. |  |
|**resolvedReason** | **String** | Always null here: only open alerts are listed. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| WARNING | &quot;warning&quot; |
| CRITICAL | &quot;critical&quot; |



