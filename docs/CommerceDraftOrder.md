

# CommerceDraftOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**invoiceUrl** | **String** | The checkout link the buyer pays through. |  [optional] |
|**invoiceSentAt** | **OffsetDateTime** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**customerId** | **String** |  |  [optional] |
|**note** | **String** |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**currency** | **String** | The currency the buyer pays in; every amount uses it. |  [optional] |
|**subtotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**discountTotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**shippingTotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**taxTotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**total** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**lineItems** | [**List&lt;CommerceDraftOrderLineItemsInner&gt;**](CommerceDraftOrderLineItemsInner.md) |  |  [optional] |
|**shippingAddress** | [**CommerceAddress**](CommerceAddress.md) |  |  [optional] |
|**orderId** | **String** | The order it became once completed. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**completedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |
| WOOCOMMERCE | &quot;woocommerce&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| INVOICE_SENT | &quot;invoice_sent&quot; |
| COMPLETED | &quot;completed&quot; |



