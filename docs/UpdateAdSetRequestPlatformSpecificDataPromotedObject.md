

# UpdateAdSetRequestPlatformSpecificDataPromotedObject

Meta ad-set promoted_object (same shape as /v1/ads/create). Meta makes promoted_object immutable once the ad set exists, so only `pixelId`, `customEventType`, `customEventStr` (with `customEventType` OTHER), `applicationId` and `productCatalogId` can be sent here.  Any other key (`pageId`, `whatsappPhoneNumber`, `customConversionId`, `objectStoreUrl`, `productSetId`, `offlineConversionDataSetId`) is a 400 with `param: platformSpecificData.promotedObject` and nothing is written. Changing them needs a new ad set (POST /v1/ads/create).  Unknown keys are rejected with 400. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pixelId** | **String** |  |  [optional] |
|**customEventType** | **String** |  |  [optional] |
|**customEventStr** | **String** | Pixel custom-event name (custom_event_str); requires customEventType OTHER. Same pairing rules as /v1/ads/create. |  [optional] |
|**pageId** | **String** |  |  [optional] |
|**applicationId** | **String** |  |  [optional] |
|**objectStoreUrl** | **String** |  |  [optional] |
|**customConversionId** | **String** |  |  [optional] |
|**productCatalogId** | **String** |  |  [optional] |
|**productSetId** | **String** |  |  [optional] |
|**offlineConversionDataSetId** | **String** |  |  [optional] |
|**whatsappPhoneNumber** | **String** |  |  [optional] |



