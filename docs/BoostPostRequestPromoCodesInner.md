

# BoostPostRequestPromoCodesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**discountType** | [**DiscountTypeEnum**](#DiscountTypeEnum) |  |  |
|**discountValue** | **BigDecimal** | PERCENTAGE: integer 1-100. CASH: amount greater than 0 in discountCurrency. |  |
|**discountCurrency** | **String** | ISO 4217; required for CASH. |  [optional] |
|**promoCode** | **String** | Code entered at checkout; omit for an automatic offer. |  [optional] |
|**minimumPurchaseType** | [**MinimumPurchaseTypeEnum**](#MinimumPurchaseTypeEnum) |  |  [optional] |
|**minimumPurchaseValue** | **BigDecimal** | Required with minimumPurchaseType; QUANTITY is an integer &gt;&#x3D; 0, SUBTOTAL an amount &gt; 0. |  [optional] |
|**minimumPurchaseCurrency** | **String** | ISO 4217; required for SUBTOTAL. |  [optional] |



## Enum: DiscountTypeEnum

| Name | Value |
|---- | -----|
| PERCENTAGE | &quot;PERCENTAGE&quot; |
| CASH | &quot;CASH&quot; |



## Enum: MinimumPurchaseTypeEnum

| Name | Value |
|---- | -----|
| QUANTITY | &quot;QUANTITY&quot; |
| SUBTOTAL | &quot;SUBTOTAL&quot; |



