

# WebhookPayloadAdVideoProcessed

Webhook payload for the `ad.video.processed` event. Fires once per `POST /v1/ads/videos` call made with `async: true`, when Meta finishes processing the video (Meta only). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. |  |
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadAdVideoProcessedAccount**](WebhookPayloadAdVideoProcessedAccount.md) |  |  |
|**video** | [**WebhookPayloadAdVideoProcessedVideo**](WebhookPayloadAdVideoProcessedVideo.md) |  |  |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| AD_VIDEO_PROCESSED | &quot;ad.video.processed&quot; |



