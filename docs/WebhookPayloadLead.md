

# WebhookPayloadLead

Webhook payload for lead.received events (Meta Lead Gen / Instant Forms).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**lead** | [**WebhookPayloadLeadLead**](WebhookPayloadLeadLead.md) |  |  |
|**account** | [**WebhookPayloadLeadAccount**](WebhookPayloadLeadAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| LEAD_RECEIVED | &quot;lead.received&quot; |



