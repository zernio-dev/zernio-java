

# AutomationTemplateInstallRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputs** | **Map&lt;String, Object&gt;** | A value for each input, by its &#x60;key&#x60;. Required inputs without a default must be sent. |  [optional] |
|**targets** | [**List&lt;AutomationTemplateInstallRequestTargetsInner&gt;**](AutomationTemplateInstallRequestTargetsInner.md) | Install several times in one call, for example on many ad accounts. Each target is its own install, all or nothing, and its &#x60;inputs&#x60; win over the shared &#x60;inputs&#x60;. A failed target leaves the others in place. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of every automation created. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



