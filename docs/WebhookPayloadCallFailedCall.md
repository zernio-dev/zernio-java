

# WebhookPayloadCallFailedCall


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**metaCallId** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**phoneNumberId** | **String** |  |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**from** | **String** |  |  [optional] |
|**to** | **String** |  |  [optional] |
|**failedAt** | **OffsetDateTime** |  |  [optional] |
|**error** | [**WebhookPayloadCallFailedCallError**](WebhookPayloadCallFailedCallError.md) |  |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;inbound&quot; |
| OUTBOUND | &quot;outbound&quot; |



