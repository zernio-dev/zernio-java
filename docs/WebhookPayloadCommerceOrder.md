

# WebhookPayloadCommerceOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** |  |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**store** | [**WebhookPayloadCommerceProductStore**](WebhookPayloadCommerceProductStore.md) |  |  [optional] |
|**resource** | [**WebhookPayloadCommerceOrderResource**](WebhookPayloadCommerceOrderResource.md) |  |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| COMMERCE_ORDER_CREATED | &quot;commerce.order.created&quot; |
| COMMERCE_ORDER_UPDATED | &quot;commerce.order.updated&quot; |
| COMMERCE_ORDER_REFUNDED | &quot;commerce.order.refunded&quot; |



