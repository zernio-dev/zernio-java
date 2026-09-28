

# GrantBusinessPartnerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**businessId** | **String** | Meta business portfolio id of the partner (numeric string). |  |
|**permittedTasks** | [**List&lt;PermittedTasksEnum&gt;**](#List&lt;PermittedTasksEnum&gt;) | Tasks granted on the Page. Defaults to ADVERTISE and ANALYZE. |  [optional] |



## Enum: List&lt;PermittedTasksEnum&gt;

| Name | Value |
|---- | -----|
| MANAGE | &quot;MANAGE&quot; |
| CREATE_CONTENT | &quot;CREATE_CONTENT&quot; |
| MODERATE | &quot;MODERATE&quot; |
| MESSAGING | &quot;MESSAGING&quot; |
| ADVERTISE | &quot;ADVERTISE&quot; |
| ANALYZE | &quot;ANALYZE&quot; |



