

# CreateCommerceDiscountRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**title** | **String** |  |  |
|**method** | [**MethodEnum**](#MethodEnum) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**code** | **String** | Required for method code. |  [optional] |
|**percentage** | **BigDecimal** | For type percentage, e.g. 15 for 15%. |  [optional] |
|**amount** | **String** | For type fixed_amount, a decimal in the store currency. |  [optional] |
|**appliesOnEachItem** | **Boolean** | fixed_amount only: take the amount off each item instead of once per order. |  [optional] |
|**minimumSubtotal** | **String** | Minimum order subtotal, a decimal in the store currency. |  [optional] |
|**minimumQuantity** | **Integer** |  |  [optional] |
|**usageLimit** | **Integer** | Code discounts only: total uses allowed. |  [optional] |
|**oncePerCustomer** | **Boolean** | Code discounts only. |  [optional] |
|**startsAt** | **OffsetDateTime** | Defaults to now. |  [optional] |
|**endsAt** | **OffsetDateTime** |  |  [optional] |
|**productIds** | **List&lt;String&gt;** |  |  [optional] |
|**collectionIds** | **List&lt;String&gt;** |  |  [optional] |
|**customerIds** | **List&lt;String&gt;** | Only these customers can use the code (&#x60;customer.id&#x60; on an order, or &#x60;id&#x60; from the customers endpoints). Code discounts on Shopify only; WooCommerce answers 400. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| CODE | &quot;code&quot; |
| AUTOMATIC | &quot;automatic&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PERCENTAGE | &quot;percentage&quot; |
| FIXED_AMOUNT | &quot;fixed_amount&quot; |
| FREE_SHIPPING | &quot;free_shipping&quot; |



