

# WebhookPayloadBalanceEmpty


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**balance** | [**WebhookPayloadBalanceEmptyBalance**](WebhookPayloadBalanceEmptyBalance.md) |  |  |
|**code** | [**CodeEnum**](#CodeEnum) | The 402 code pay-per-use calls get until the balance is funded. &#x60;usage_limit_reached&#x60; when the auto top-up monthly limit is what keeps it at $0. |  |
|**fundingUrl** | **URI** | Dashboard link that opens the top-up drawer in Billing. |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event. Retries and redeliveries keep the original value. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| BALANCE_EMPTY | &quot;balance.empty&quot; |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| INSUFFICIENT_BALANCE | &quot;insufficient_balance&quot; |
| USAGE_LIMIT_REACHED | &quot;usage_limit_reached&quot; |



