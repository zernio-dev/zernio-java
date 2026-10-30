

# WebhookPayloadReviewDeleted

Webhook payload for the review.deleted event.  Google Business Profile stopped returning this review, for example after Google's spam filter removed it. Detected by polling: fires usually 6 to 12 hours after the review disappears, only for locations covered by a webhook subscribed to review.deleted or review.restored. If the review comes back, review.restored fires. May arrive for a review id you never received review.new for. A review hidden and restored by Google may produce review.deleted followed by review.restored, and a review.updated can arrive for a review previously reported by review.deleted (it is restored on the next check). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**review** | [**WebhookPayloadReviewDeletedReview**](WebhookPayloadReviewDeletedReview.md) |  |  |
|**account** | [**WebhookPayloadReviewNewAccount**](WebhookPayloadReviewNewAccount.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| REVIEW_DELETED | &quot;review.deleted&quot; |



