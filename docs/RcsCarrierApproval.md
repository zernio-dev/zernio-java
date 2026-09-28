

# RcsCarrierApproval


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approvalId** | **String** |  |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**carrier** | **String** |  |  [optional] |
|**approvedAt** | **OffsetDateTime** |  |  [optional] |
|**rejectedReason** | **String** |  |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| CARRIER | &quot;carrier&quot; |
| HUB | &quot;hub&quot; |
| BOT | &quot;bot&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| SUBMITTED | &quot;SUBMITTED&quot; |
| APPROVED | &quot;APPROVED&quot; |
| REJECTED | &quot;REJECTED&quot; |



