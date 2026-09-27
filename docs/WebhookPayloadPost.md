

# WebhookPayloadPost

Webhook payload for post events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**post** | [**WebhookPayloadPostPost**](WebhookPayloadPostPost.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| POST_SCHEDULED | &quot;post.scheduled&quot; |
| POST_PUBLISHED | &quot;post.published&quot; |
| POST_FAILED | &quot;post.failed&quot; |
| POST_PARTIAL | &quot;post.partial&quot; |
| POST_CANCELLED | &quot;post.cancelled&quot; |
| POST_RECYCLED | &quot;post.recycled&quot; |



