

# PreflightSmsRegistration200ResponseAdvisoriesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | **String** | The payload field the finding is about, when attributable. |  [optional] |
|**code** | **String** | Stable rule id for deterministic findings; absent on AI findings. |  [optional] |
|**concern** | **String** |  |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| BLOCK | &quot;block&quot; |
| WARN | &quot;warn&quot; |



