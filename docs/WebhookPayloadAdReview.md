

# WebhookPayloadAdReview

Webhook payload for the `ad.review.approved` and `ad.review.rejected` events. Emitted for every ad network Zernio syncs (Meta, Google, TikTok, LinkedIn, Pinterest, X and the rest).  Fires when an ad Zernio already tracked changes review outcome:  - `approved`: it leaves review as deliverable, or a rejection is overturned. - `rejected`: the platform rejects it.  Ads seen for the first time by a sync, including the history loaded when an account is connected, never fire it. An ad that leaves review paused (for example its ad set is paused) sends no `approved` event.  Detected by Zernio's own ad sync (and, for Meta, the review poll), so it arrives within one sync cycle of the platform's decision, not instantly. Each outcome is delivered at most once per ad per 24 hours. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Use it to route the event to your tenant without storing Zernio profile ids.  Present on every event tied to a profile, absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once.  |  [optional] |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookAdsAccount**](WebhookAdsAccount.md) |  |  |
|**adObject** | [**WebhookPayloadAdReviewAdObject**](WebhookPayloadAdReviewAdObject.md) |  |  |
|**review** | [**WebhookPayloadAdReviewReview**](WebhookPayloadAdReviewReview.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| AD_REVIEW_APPROVED | &quot;ad.review.approved&quot; |
| AD_REVIEW_REJECTED | &quot;ad.review.rejected&quot; |



