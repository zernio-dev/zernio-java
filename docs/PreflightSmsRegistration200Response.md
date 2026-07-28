

# PreflightSmsRegistration200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**composed** | [**PreflightSmsRegistration200ResponseComposed**](PreflightSmsRegistration200ResponseComposed.md) |  |  [optional] |
|**advisories** | [**List&lt;PreflightSmsRegistration200ResponseAdvisoriesInner&gt;**](PreflightSmsRegistration200ResponseAdvisoriesInner.md) |  |  [optional] |
|**verdict** | [**VerdictEnum**](#VerdictEnum) |  |  [optional] |
|**aiUnavailable** | **Boolean** | True when the AI portion of the check could not run; advisories then contain only deterministic findings. |  [optional] |



## Enum: VerdictEnum

| Name | Value |
|---- | -----|
| PASS | &quot;pass&quot; |
| WARN | &quot;warn&quot; |
| FAIL | &quot;fail&quot; |
| UNREVIEWED | &quot;unreviewed&quot; |



