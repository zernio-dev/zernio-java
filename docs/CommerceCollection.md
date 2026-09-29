

# CommerceCollection

A product collection on a connected store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native collection id. |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**handle** | **String** |  |  [optional] |
|**descriptionHtml** | **String** |  |  [optional] |
|**image** | [**CommerceImage**](CommerceImage.md) |  |  [optional] |
|**sortOrder** | [**SortOrderEnum**](#SortOrderEnum) |  |  [optional] |
|**productCount** | **Integer** | Updates a few seconds after a membership change. |  [optional] |
|**seo** | [**ProductSeo**](ProductSeo.md) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**platformData** | **Map&lt;String, Object&gt;** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |
| WOOCOMMERCE | &quot;woocommerce&quot; |



## Enum: SortOrderEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;manual&quot; |
| BEST_SELLING | &quot;best_selling&quot; |
| ALPHA_ASC | &quot;alpha_asc&quot; |
| ALPHA_DESC | &quot;alpha_desc&quot; |
| PRICE_ASC | &quot;price_asc&quot; |
| PRICE_DESC | &quot;price_desc&quot; |
| CREATED | &quot;created&quot; |
| CREATED_DESC | &quot;created_desc&quot; |
| MOST_RELEVANT | &quot;most_relevant&quot; |



