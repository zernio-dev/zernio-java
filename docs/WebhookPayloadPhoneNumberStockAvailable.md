

# WebhookPayloadPhoneNumberStockAvailable

Webhook payload for phone_number.stock_available events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**stock** | [**WebhookPayloadPhoneNumberStockAvailableStock**](WebhookPayloadPhoneNumberStockAvailableStock.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| PHONE_NUMBER_STOCK_AVAILABLE | &quot;phone_number.stock_available&quot; |



