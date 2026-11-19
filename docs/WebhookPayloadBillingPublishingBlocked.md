

# WebhookPayloadBillingPublishingBlocked


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**billing** | [**WebhookPayloadBillingPublishingBlockedBilling**](WebhookPayloadBillingPublishingBlockedBilling.md) |  |  |
|**billingUrl** | **URI** | Dashboard page where the owner pays or replaces the card. |  |
|**timestamp** | **OffsetDateTime** |  |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| BILLING_PUBLISHING_BLOCKED | &quot;billing.publishing_blocked&quot; |



