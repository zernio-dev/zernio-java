

# AdCreativeCatalog

Meta catalog template ads created through Zernio only (absent on ads synced from Meta).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**productSetId** | **String** | The creative&#39;s product_set_id. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | object_story_spec.template_data.format_option, from catalogFormat. |  [optional] |
|**formatTransformationSpec** | [**List&lt;AdCreativeCatalogFormatTransformationSpecInner&gt;**](AdCreativeCatalogFormatTransformationSpecInner.md) | The format_transformation_spec sent on the creative, as Meta&#39;s raw objects. Present for single_image. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| SINGLE_IMAGE | &quot;single_image&quot; |
| CAROUSEL_IMAGES_MULTI_ITEMS | &quot;carousel_images_multi_items&quot; |
| CAROUSEL_IMAGES_SINGLE_ITEM | &quot;carousel_images_single_item&quot; |
| CAROUSEL_SLIDESHOWS | &quot;carousel_slideshows&quot; |



