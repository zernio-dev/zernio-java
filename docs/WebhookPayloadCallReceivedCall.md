

# WebhookPayloadCallReceivedCall


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Internal Zernio Call doc id |  [optional] |
|**metaCallId** | **String** | Meta wacid.* call id when known |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**phoneNumberId** | **String** | Meta phone_number_id |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**from** | **String** | Consumer wa_id / E.164 |  [optional] |
|**to** | **String** | Business number (E.164) |  [optional] |
|**forwardTo** | **String** | Destination snapshot at routing time |  [optional] |
|**contactId** | **String** |  |  [optional] |
|**conversationId** | **String** |  |  [optional] |
|**startedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;inbound&quot; |
| OUTBOUND | &quot;outbound&quot; |



