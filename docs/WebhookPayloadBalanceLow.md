

# WebhookPayloadBalanceLow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**balance** | [**WebhookPayloadBalanceLowBalance**](WebhookPayloadBalanceLowBalance.md) |  |  |
|**fundingUrl** | **URI** | Dashboard link that opens the Add funds drawer in Billing. |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event. Retries and redeliveries keep the original value. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| BALANCE_LOW | &quot;balance.low&quot; |



