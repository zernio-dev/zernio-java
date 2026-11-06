

# AutomationApproval

A request an automation sent for a person's approval before acting, with each change it holds.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**automationId** | **String** |  |  |
|**checkId** | **String** | The check that found the matches and sent the request. |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;cancelled&#x60; when the automation stopped asking for approval before anyone decided. |  |
|**to** | **List&lt;String&gt;** | The emails the request was sent to. |  |
|**expiresAt** | **OffsetDateTime** | After this the request can no longer be decided and its changes are skipped. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**decidedBy** | [**AutomationApprovalDecidedBy**](AutomationApprovalDecidedBy.md) |  |  |
|**decidedAt** | **OffsetDateTime** |  |  |
|**canDecide** | **Boolean** | True when the request is pending and you are one of the approvers the automation names now. |  |
|**changes** | [**List&lt;AutomationApprovalChange&gt;**](AutomationApprovalChange.md) | The changes the request holds. Notifications are not listed. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |
| EXPIRED | &quot;expired&quot; |
| CANCELLED | &quot;cancelled&quot; |



