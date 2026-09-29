

# CommerceProduct

A product on a connected store, in the platform-neutral shape.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native product id. |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**descriptionHtml** | **String** |  |  [optional] |
|**handle** | **String** | URL slug of the product. |  [optional] |
|**vendor** | **String** |  |  [optional] |
|**productType** | **String** |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**status** | **CommerceProductStatus** |  |  [optional] |
|**platformStatus** | **String** | The raw status on the platform, e.g. ACTIVE on Shopify. |  [optional] |
|**featuredImage** | [**CommerceImage**](CommerceImage.md) |  |  [optional] |
|**images** | [**List&lt;CommerceImage&gt;**](CommerceImage.md) | First 20 images, in store order. |  [optional] |
|**options** | [**List&lt;ProductOptionsInner&gt;**](ProductOptionsInner.md) | Option axes (e.g. Size, Color) and their values. |  [optional] |
|**variants** | [**List&lt;CommerceVariant&gt;**](CommerceVariant.md) | First 100 variants. |  [optional] |
|**totalInventory** | **Integer** |  |  [optional] |
|**url** | **String** | Public storefront URL; null while the product is not published. |  [optional] |
|**seo** | [**ProductSeo**](ProductSeo.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**publishedAt** | **OffsetDateTime** |  |  [optional] |
|**platformData** | **Map&lt;String, Object&gt;** | Platform-only fields. Null when the platform has none. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |



