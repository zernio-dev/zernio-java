

# CommerceOrderLineItemsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**productId** | **String** | Null when the product was deleted. |  [optional] |
|**variantId** | **String** |  |  [optional] |
|**sku** | **String** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**variantTitle** | **String** |  |  [optional] |
|**quantity** | **Integer** | As ordered; refunded units are listed under refunds. |  [optional] |
|**unitPrice** | [**CommerceMoney**](CommerceMoney.md) | Before discounts. |  [optional] |
|**subtotal** | [**CommerceMoney**](CommerceMoney.md) | unitPrice x quantity. |  [optional] |
|**discountTotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**total** | [**CommerceMoney**](CommerceMoney.md) | subtotal minus discountTotal. |  [optional] |
|**taxLines** | [**List&lt;CommerceTaxLine&gt;**](CommerceTaxLine.md) |  |  [optional] |



