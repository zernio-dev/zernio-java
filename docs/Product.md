

# Product

A product on the connected platform with its variants, options and images. All data lives on the platform; Zernio proxies it and stores nothing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native product id (numeric string for Shopify). |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**handle** | **String** | URL slug of the product. |  [optional] |
|**descriptionHtml** | **String** | Product description as HTML. |  [optional] |
|**vendor** | **String** |  |  [optional] |
|**productType** | **String** | Free-text product type as set on the store. |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**featuredImage** | [**ProductImage**](ProductImage.md) |  |  [optional] |
|**images** | [**List&lt;ProductImage&gt;**](ProductImage.md) | First 20 images in the product media, in store order. |  [optional] |
|**options** | [**List&lt;ProductOptionsInner&gt;**](ProductOptionsInner.md) | Option axes (e.g. Size, Color) and their values. |  [optional] |
|**variants** | [**List&lt;ProductVariant&gt;**](ProductVariant.md) | First 100 variants. |  [optional] |
|**seo** | [**ProductSeo**](ProductSeo.md) |  |  [optional] |
|**totalInventory** | **Integer** |  |  [optional] |
|**onlineStoreUrl** | **String** | Public storefront URL; null while the product is not published to the online store. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**publishedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DRAFT | &quot;draft&quot; |
| ARCHIVED | &quot;archived&quot; |



