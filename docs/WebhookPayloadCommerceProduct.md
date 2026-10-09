

# WebhookPayloadCommerceProduct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** |  |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**store** | [**WebhookPayloadCommerceProductStore**](WebhookPayloadCommerceProductStore.md) |  |  [optional] |
|**resource** | [**WebhookPayloadCommerceProductResource**](WebhookPayloadCommerceProductResource.md) |  |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| COMMERCE_PRODUCT_CREATED | &quot;commerce.product.created&quot; |
| COMMERCE_PRODUCT_UPDATED | &quot;commerce.product.updated&quot; |
| COMMERCE_PRODUCT_DELETED | &quot;commerce.product.deleted&quot; |



