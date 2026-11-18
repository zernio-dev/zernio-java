

# CreateStandaloneAdRequestCarouselCardsInner

Exactly one of `imageUrl` or `video` (a 400 otherwise).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageUrl** | **URI** | Image card: the card image, uploaded to the ad account and referenced by hash. |  [optional] |
|**video** | [**CreateStandaloneAdRequestCarouselCardsInnerVideo**](CreateStandaloneAdRequestCarouselCardsInnerVideo.md) |  |  [optional] |
|**linkUrl** | **URI** | Card destination URL. Defaults to the top-level linkUrl, or Meta&#39;s lead-form link when leadGenFormId is set and neither is provided. |  [optional] |
|**headline** | **String** | Card headline, shown below the card image. |  [optional] |
|**description** | **String** | Card description, shown under the headline. |  [optional] |
|**callToAction** | **String** | Card CTA override. Defaults to the top-level callToAction; same enum. |  [optional] |



