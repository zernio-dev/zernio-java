

# AutomationApprovalStep

Makes the ad rule wait for a person's OK before it acts. One per ad rule, placed before the change. Each change waits until one of `to` approves it, for `expiresIn` at most. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**to** | **List&lt;String&gt;** | Team members, by email. Each once. |  |
|**expiresIn** | **String** | From &#x60;15m&#x60; to &#x60;7d&#x60;, in whole minutes. |  |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| APPROVAL | &quot;approval&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| APPROVAL_REQUEST | &quot;approval.request&quot; |



