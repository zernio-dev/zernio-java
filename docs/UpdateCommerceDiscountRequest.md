

# UpdateCommerceDiscountRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**title** | **String** |  |  [optional] |
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



