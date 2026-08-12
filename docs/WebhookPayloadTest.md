

# WebhookPayloadTest

Webhook payload for test deliveries

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**message** | **String** | Human-readable test message |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this test event (set once when the payload is built). Test fires are sent synchronously as a single attempt; a later redelivery of this event keeps the original value. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| WEBHOOK_TEST | &quot;webhook.test&quot; |



