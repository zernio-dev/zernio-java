

# WebhookPayloadSupportRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Event id, the dedupe key. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |
|**run** | [**SupportRun**](SupportRun.md) |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| SUPPORT_RUN_COMPLETED | &quot;support.run.completed&quot; |
| SUPPORT_RUN_FAILED | &quot;support.run.failed&quot; |



