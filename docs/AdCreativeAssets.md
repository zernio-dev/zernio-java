

# AdCreativeAssets

Google Display only. Native Google asset resource name of each image on the responsive display ad, keyed by Google's image role. Set at creation for ads created through Zernio. PUT /v1/ads/{adId} overwrites only the role it replaces: `creative.imageUrl` updates `marketingImages`, `creative.squareImageUrl` updates `squareMarketingImages`. Absent on ads synced from Google.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**marketingImages** | [**List&lt;AdCreativeAssetsMarketingImagesInner&gt;**](AdCreativeAssetsMarketingImagesInner.md) | Landscape (1.91:1) marketing images. The first item matches &#x60;assetResourceName&#x60;. |  [optional] |
|**squareMarketingImages** | [**List&lt;AdCreativeAssetsSquareMarketingImagesInner&gt;**](AdCreativeAssetsSquareMarketingImagesInner.md) | Square (1:1) marketing images. |  [optional] |



