

# WebhookPayloadSupportRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Event id, the dedupe key. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |
|**run** | [**SupportRun**](SupportRun.md) |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| SUPPORT_RUN_COMPLETED | &quot;support.run.completed&quot; |
| SUPPORT_RUN_FAILED | &quot;support.run.failed&quot; |



