

# GoogleListingGroupFilterNode


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**resourceName** | **String** | customers/{customerId}/assetGroupListingGroupFilters/{assetGroupId}~{filterId} |  |
|**parentResourceName** | **String** | Null for the root node. |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**listingSource** | **String** |  |  |
|**dimension** | **Object** | Google&#39;s case value for the node, such as { productBrand: { value: &#39;Acme&#39; } }. A dimension with no value is the everything-else node. Null for the root. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SUBDIVISION | &quot;SUBDIVISION&quot; |
| UNIT_INCLUDED | &quot;UNIT_INCLUDED&quot; |
| UNIT_EXCLUDED | &quot;UNIT_EXCLUDED&quot; |



