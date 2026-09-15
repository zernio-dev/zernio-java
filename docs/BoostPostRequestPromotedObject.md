

# BoostPostRequestPromotedObject

TikTok-only on this endpoint. The pixel a Website Conversion ad group optimizes toward, so a Spark Ad built from an existing organic post can optimize for a conversion instead of only engagement or traffic.  Required when `goal` is `conversions`, and BOTH fields are required: TikTok refuses a conversion ad group with no pixel (\"Please select a pixel\") and equally one that has a pixel but no event (\"Select a pixel event.\"), because the event is what the ad group optimizes toward. Ignored on every other goal, since only a WEB_CONVERSIONS ad group accepts them.  Combine freely with `platformPostId` + `sparkAuthCode`: the pixel lives on the ad group and the Spark item on the creative, so they never conflict. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pixelId** | **String** | TikTok Pixel. Either the numeric pixel id or the alphanumeric pixel code from Events Manager, which is resolved for you. |  |
|**customEventType** | **String** | Optimization event, as a TikTok optimization_event code (e.g. ON_WEB_ORDER, SHOPPING, FORM) or the exact event name shown in Events Manager, which is resolved to its code. The event must already exist on that pixel, or TikTok rejects the ad group. |  |



