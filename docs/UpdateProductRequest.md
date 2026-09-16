

# UpdateProductRequest

At least one field is required.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  [optional] |
|**descriptionHtml** | **String** | Product description as HTML. |  [optional] |
|**handle** | **String** | URL slug of the product. |  [optional] |
|**vendor** | **String** |  |  [optional] |
|**productType** | **String** |  |  [optional] |
|**tags** | **List&lt;String&gt;** | Replaces the full tag list. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | archived hides the product everywhere; draft keeps it editable but unpublished. |  [optional] |
|**seo** | [**UpdateProductRequestSeo**](UpdateProductRequestSeo.md) |  |  [optional] |
|**variants** | [**List&lt;UpdateProductRequestVariantsInner&gt;**](UpdateProductRequestVariantsInner.md) | Price changes per variant. Only the listed variants change. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DRAFT | &quot;draft&quot; |
| ARCHIVED | &quot;archived&quot; |



