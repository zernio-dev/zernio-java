

# BoostPostRequestPromotedObject

TikTok-only on this endpoint. The pixel a Website Conversion ad group optimizes toward, so a Spark Ad built from an existing organic post can optimize for a conversion instead of only engagement or traffic. Required when `goal` is `conversions`; ignored on every other goal, because only a WEB_CONVERSIONS ad group accepts these fields.  Combine freely with `platformPostId` + `sparkAuthCode`: the pixel lives on the ad group and the Spark item on the creative, so they never conflict. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pixelId** | **String** | TikTok Pixel. Either the numeric pixel id or the alphanumeric pixel code from Events Manager, which is resolved for you. |  [optional] |
|**customEventType** | **String** | Optimization event, as a TikTok optimization_event code (e.g. ON_WEB_ORDER, SHOPPING, FORM) or the exact event name shown in Events Manager, which is resolved to its code. Omit to let TikTok optimize for the ad group default. |  [optional] |



