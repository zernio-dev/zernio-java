

# ProductVariant

A purchasable variant of a product (one per option combination).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native variant id (numeric string for Shopify). |  [optional] |
|**title** | **String** | Option combination label, e.g. \&quot;S / Blue\&quot;. |  [optional] |
|**sku** | **String** |  |  [optional] |
|**barcode** | **String** |  |  [optional] |
|**price** | **String** | Decimal amount in the store currency, e.g. \&quot;19.90\&quot;. |  [optional] |
|**compareAtPrice** | **String** | Strike-through price; null when the variant is not on sale. |  [optional] |
|**inventoryQuantity** | **Integer** | Units on hand across locations; null when inventory is not tracked. |  [optional] |
|**availableForSale** | **Boolean** |  |  [optional] |
|**selectedOptions** | [**List&lt;ProductVariantSelectedOptionsInner&gt;**](ProductVariantSelectedOptionsInner.md) |  |  [optional] |



