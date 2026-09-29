

# UpdateCommerceCollectionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**title** | **String** |  |  [optional] |
|**descriptionHtml** | **String** |  |  [optional] |
|**handle** | **String** |  |  [optional] |
|**sortOrder** | [**SortOrderEnum**](#SortOrderEnum) |  |  [optional] |
|**seo** | [**CreateCommerceProductRequestSeo**](CreateCommerceProductRequestSeo.md) |  |  [optional] |
|**image** | [**CreateCommerceProductRequestImagesInner**](CreateCommerceProductRequestImagesInner.md) |  |  [optional] |



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



