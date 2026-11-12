

# CreateCommerceDraftOrderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Connected store SocialAccount id. |  |
|**customerId** | **String** | The customer it is for, from the customers endpoints. |  [optional] |
|**email** | **String** |  |  [optional] |
|**lineItems** | [**List&lt;CreateCommerceDraftOrderRequestLineItemsInner&gt;**](CreateCommerceDraftOrderRequestLineItemsInner.md) | A product variant (variantId) or a custom item (title and price). |  |
|**discount** | [**CreateCommerceDraftOrderRequestDiscount**](CreateCommerceDraftOrderRequestDiscount.md) |  |  [optional] |
|**shipping** | [**CreateCommerceDraftOrderRequestShipping**](CreateCommerceDraftOrderRequestShipping.md) |  |  [optional] |
|**shippingAddress** | [**CreateCommerceDraftOrderRequestShippingAddress**](CreateCommerceDraftOrderRequestShippingAddress.md) |  |  [optional] |
|**note** | **String** |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |



