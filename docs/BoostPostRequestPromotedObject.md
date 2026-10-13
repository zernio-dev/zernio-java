

# BoostPostRequestPromotedObject

Meta, TikTok and Reddit. What the conversion ad set optimizes toward, so a boost of an existing organic post can run for a conversion instead of only engagement or traffic. Required when `goal` is `conversions` (Meta also `lead_conversion`); ignored on goals that do not optimize for a conversion.  Meta: `pixelId` + `customEventType` (a commerce event such as PURCHASE under `conversions`, a leads-class event such as LEAD under `lead_conversion`), or `customConversionId` to optimize against a Custom Conversion, or `customEventType: OTHER` + `customEventStr` for a pixel custom event. Becomes the ad set `promoted_object`; without it Meta rejects the ad set (\"Please select a promoted object\", subcode 1815430). With `adSetId` the existing ad set already carries it.  TikTok: BOTH `pixelId` and `customEventType` are required. TikTok refuses a conversion ad group with no pixel (\"Please select a pixel\") and one with a pixel but no event (\"Select a pixel event.\"). Combine freely with `platformPostId` + `sparkAuthCode`: the pixel lives on the ad group and the Spark item on the creative.  Reddit: every ad group carries a pixel, whatever the goal. `pixelId` picks it (default: the ad account's first pixel; 422 when the account has none). `conversions` requires `customEventType` (PURCHASE, LEAD, COMPLETE_REGISTRATION, SIGN_UP, ADD_TO_CART, PAGE_VISIT, VIEW_CONTENT or CONTENT_VIEW), and the pixel must already have received that event (422 otherwise); `lead_generation` needs the pixel to have received Lead. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pixelId** | **String** | Meta Pixel id, TikTok Pixel (numeric id or the alphanumeric pixel code from Events Manager, resolved for you), or Reddit pixel id. |  [optional] |
|**customEventType** | **String** | Meta: standard pixel event (PURCHASE, LEAD, ...) or OTHER with customEventStr. TikTok: optimization_event code (e.g. ON_WEB_ORDER, SHOPPING, FORM) or the exact event name shown in Events Manager, resolved to its code; the event must already exist on that pixel. |  [optional] |
|**customEventStr** | **String** | Meta only. Pixel custom event name as it appears in Events Manager; requires customEventType OTHER. |  [optional] |
|**customConversionId** | **String** | Meta only. Custom Conversion to optimize against, instead of pixelId + customEventType. |  [optional] |



