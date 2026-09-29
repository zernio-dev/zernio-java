

# CreateCommerceProductRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**title** | **String** |  |  |
|**descriptionHtml** | **String** |  |  [optional] |
|**handle** | **String** |  |  [optional] |
|**vendor** | **String** |  |  [optional] |
|**productType** | **String** |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**seo** | [**CreateCommerceProductRequestSeo**](CreateCommerceProductRequestSeo.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**images** | [**List&lt;CreateCommerceProductRequestImagesInner&gt;**](CreateCommerceProductRequestImagesInner.md) |  |  [optional] |
|**options** | [**List&lt;CreateCommerceProductRequestOptionsInner&gt;**](CreateCommerceProductRequestOptionsInner.md) |  |  [optional] |
|**variants** | [**List&lt;CreateCommerceProductRequestVariantsInner&gt;**](CreateCommerceProductRequestVariantsInner.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |



