

# WebhookPayloadLead

Webhook payload for lead.received events (Meta Lead Gen / Instant Forms).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**lead** | [**WebhookPayloadLeadLead**](WebhookPayloadLeadLead.md) |  |  |
|**account** | [**WebhookPayloadLeadAccount**](WebhookPayloadLeadAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| LEAD_RECEIVED | &quot;lead.received&quot; |



