

# CommerceOrder

An order with what an invoice needs. Every amount is in `currency`, the store currency.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**number** | **String** | The number the merchant and buyer see. |  [optional] |
|**status** | **CommerceOrderStatus** |  |  [optional] |
|**platformStatus** | **String** | Shopify fulfilment status (e.g. UNFULFILLED) or WooCommerce order status (e.g. processing). |  [optional] |
|**paymentStatus** | [**PaymentStatusEnum**](#PaymentStatusEnum) |  |  [optional] |
|**platformPaymentStatus** | **String** | Shopify financial status. Null on WooCommerce, where payment is read from the order status. |  [optional] |
|**currency** | **String** |  |  [optional] |
|**taxesIncluded** | **Boolean** | Whether line item and shipping amounts include tax. Always false on WooCommerce, whose API returns amounts before tax whatever the store displays (platformData.pricesIncludeTax). |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**paidAt** | **OffsetDateTime** | WooCommerce only; null on Shopify. |  [optional] |
|**cancelledAt** | **OffsetDateTime** | Shopify only; null on WooCommerce. |  [optional] |
|**cancelReason** | **String** |  |  [optional] |
|**subtotal** | [**CommerceMoney**](CommerceMoney.md) | Line items before order discounts and shipping. |  [optional] |
|**discountTotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**shippingTotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**taxTotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**total** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**refundedTotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**discountCodes** | **List&lt;String&gt;** |  |  [optional] |
|**paymentMethods** | **List&lt;String&gt;** |  |  [optional] |
|**customer** | [**CommerceOrderCustomer**](CommerceOrderCustomer.md) |  |  [optional] |
|**billingAddress** | [**CommerceAddress**](CommerceAddress.md) |  |  [optional] |
|**shippingAddress** | [**CommerceAddress**](CommerceAddress.md) |  |  [optional] |
|**buyerNote** | **String** |  |  [optional] |
|**lineItems** | [**List&lt;CommerceOrderLineItemsInner&gt;**](CommerceOrderLineItemsInner.md) |  |  [optional] |
|**shippingLines** | [**List&lt;CommerceOrderChargeLine&gt;**](CommerceOrderChargeLine.md) |  |  [optional] |
|**feeLines** | [**List&lt;CommerceOrderChargeLine&gt;**](CommerceOrderChargeLine.md) | WooCommerce fees. Always empty on Shopify. |  [optional] |
|**taxLines** | [**List&lt;CommerceTaxLine&gt;**](CommerceTaxLine.md) | Order tax by rate, line items and shipping together. |  [optional] |
|**refunds** | [**List&lt;CommerceOrderRefundsInner&gt;**](CommerceOrderRefundsInner.md) |  |  [optional] |
|**fulfillments** | [**List&lt;CommerceOrderFulfillmentsInner&gt;**](CommerceOrderFulfillmentsInner.md) |  |  [optional] |
|**platformData** | **Map&lt;String, Object&gt;** | Platform-only fields. Null when the platform has none. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |
| WOOCOMMERCE | &quot;woocommerce&quot; |



## Enum: PaymentStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| AUTHORIZED | &quot;authorized&quot; |
| PARTIALLY_PAID | &quot;partially_paid&quot; |
| PAID | &quot;paid&quot; |
| PARTIALLY_REFUNDED | &quot;partially_refunded&quot; |
| REFUNDED | &quot;refunded&quot; |
| VOIDED | &quot;voided&quot; |
| FAILED | &quot;failed&quot; |



