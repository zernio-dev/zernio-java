

# ListSmsOptOuts200ResponseOptOutsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumber** | **String** |  |  [optional] |
|**optedOutAt** | **OffsetDateTime** |  |  [optional] |
|**keyword** | **String** | The keyword they sent (e.g. STOP), when the carrier recorded one. |  [optional] |
|**from** | **String** | Which of your numbers the recipient opted out from. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | &#x60;inbound_stop&#x60; when the recipient texted an opt-out keyword, &#x60;api&#x60; when recorded with &#x60;POST /v1/sms/opt-outs&#x60;. Null when unknown. |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| INBOUND_STOP | &quot;inbound_stop&quot; |
| API | &quot;api&quot; |



