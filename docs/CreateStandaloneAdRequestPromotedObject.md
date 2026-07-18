

# CreateStandaloneAdRequestPromotedObject

What the ad optimises against. Behaviour depends on the platform.  **Meta**: forwarded to the ad set's `promoted_object` (snake-cased). Required for goals whose ad-set optimization_goal points at a specific event/page/app (without it Meta rejects the ad-set create with `error_subcode: 1815430` \"Please select a promoted object for your ad set\"):   - `goal: conversions` (OFFSITE_CONVERSIONS): requires `pixelId` + `customEventType`   - `goal: app_promotion` (APP_INSTALLS): requires `applicationId` + `objectStoreUrl`   - `goal: lead_generation` (LEAD_GENERATION): `pageId` is auto-filled from the connected Page when omitted  Other Meta goals (engagement, traffic, awareness, video_views) ignore this field.  **TikTok**: only `goal: conversions` uses it.   - `pixelId` maps to the ad group's `pixel_id`. Required: a TikTok website-conversion     ad group without a pixel is rejected with `40002: Please select a pixel`.   - `customEventType` maps to the ad group's `optimization_event` (the pixel event to     optimise for). Optional: TikTok accepts a pixel-only auto-bid conversion ad group.     See the `customEventType` field below for the valid TikTok codes.  The remaining `promotedObject.*` fields are Meta-only. Platforms other than Meta and TikTok ignore `promotedObject` entirely. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pixelId** | **String** | Pixel ID. **Meta:** Facebook Pixel ID, required for &#x60;goal: conversions&#x60;. **TikTok:** TikTok Pixel ID, required for &#x60;goal: conversions&#x60;.  |  [optional] |
|**customEventType** | **String** | The event the campaign/ad group optimises against.  **Meta:** standard event like &#x60;PURCHASE&#x60;, &#x60;LEAD&#x60;, &#x60;COMPLETE_REGISTRATION&#x60;, &#x60;ADD_TO_CART&#x60;. Uppercased internally so callers can pass any case. Required for &#x60;goal: conversions&#x60;.  **TikTok:** an &#x60;optimization_event&#x60; code (UPPER_SNAKE, not Meta&#39;s vocabulary and not PascalCase), OR the exact event name shown in TikTok Events Manager (auto-resolved to its code). Must be one of the event types your TikTok Pixel tracks; custom events are not optimizable. Current taxonomy: &#x60;SHOPPING&#x60; (Purchase), &#x60;ON_WEB_CART&#x60; (Add to Cart), &#x60;INITIATE_ORDER&#x60; (Initiate Checkout), &#x60;FORM&#x60; (Lead), &#x60;ON_WEB_REGISTER&#x60; (Complete Registration), &#x60;ON_WEB_DETAIL&#x60; (View Content). &#x60;ON_WEB_ORDER&#x60; is deprecated. On rejection the error lists the event types your pixel actually tracks. Optional for &#x60;goal: conversions&#x60;.  |  [optional] |
|**pageId** | **String** | Facebook Page ID. Used by &#x60;goal: lead_generation&#x60;. Auto-filled from the connected Page when omitted.  |  [optional] |
|**applicationId** | **String** | App ID. Required for &#x60;goal: app_promotion&#x60;. |  [optional] |
|**objectStoreUrl** | **URI** | App Store / Play Store listing URL. Required for &#x60;goal: app_promotion&#x60;. |  [optional] |
|**customConversionId** | **String** | Custom Conversion ID, when optimising against one instead of a standard event. |  [optional] |
|**productCatalogId** | **String** | Catalog ID for catalog/Advantage+ Shopping campaigns. |  [optional] |
|**productSetId** | **String** | Product Set ID inside the catalog. |  [optional] |



