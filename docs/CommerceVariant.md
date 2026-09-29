

# CommerceVariant

A purchasable variant of a product (one per option combination).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native variant id. |  [optional] |
|**title** | **String** | Option combination label, e.g. \&quot;S / Blue\&quot;. |  [optional] |
|**sku** | **String** |  |  [optional] |
|**barcode** | **String** |  |  [optional] |
|**price** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**compareAtPrice** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**inventoryQuantity** | **Integer** | Units on hand; null when inventory is not tracked. |  [optional] |
|**availableForSale** | **Boolean** |  |  [optional] |
|**options** | [**List&lt;CreateCommerceProductVariantsRequestVariantsInnerOptionsInner&gt;**](CreateCommerceProductVariantsRequestVariantsInnerOptionsInner.md) |  |  [optional] |



