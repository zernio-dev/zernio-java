

# GoogleAssetGroupAssetLink

Link one asset to the asset group. Send exactly one of asset (an existing asset), text, imageUrl or youtubeVideoId (new content, created in the same request).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldType** | **String** | Google AssetFieldType, such as HEADLINE, LONG_HEADLINE, DESCRIPTION, BUSINESS_NAME, MARKETING_IMAGE, SQUARE_MARKETING_IMAGE, PORTRAIT_MARKETING_IMAGE, LOGO, LANDSCAPE_LOGO or YOUTUBE_VIDEO. |  |
|**asset** | **String** | Existing asset id or resource name customers/{customerId}/assets/{assetId}. Must belong to the campaign&#39;s ad account. |  [optional] |
|**text** | **String** | Text assets link as HEADLINE, LONG_HEADLINE, DESCRIPTION or BUSINESS_NAME. |  [optional] |
|**imageUrl** | **URI** | Public http(s) image. Links as an image role or LOGO / LANDSCAPE_LOGO. |  [optional] |
|**youtubeVideoId** | **String** | Links as YOUTUBE_VIDEO. |  [optional] |



