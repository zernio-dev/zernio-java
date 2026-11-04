

# WebhookPayloadAutomationAlertAlert


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**subjectId** | **String** | The platform&#39;s id of the object: an ad, ad set or campaign for ad rules. |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Why it resolved, on &#x60;automation.alert.resolved&#x60; only. |  |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| WARNING | &quot;warning&quot; |
| CRITICAL | &quot;critical&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| CONDITION_CLEARED | &quot;condition_cleared&quot; |
| ACTION_APPLIED | &quot;action_applied&quot; |
| NOT_EVALUATED | &quot;not_evaluated&quot; |
| AUTOMATION_CHANGED | &quot;automation_changed&quot; |
| AUTOMATION_OFF | &quot;automation_off&quot; |



