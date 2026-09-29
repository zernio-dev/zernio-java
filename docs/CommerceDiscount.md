

# CommerceDiscount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**codes** | **List&lt;String&gt;** | The first 10 codes; codeCount has the total. |  [optional] |
|**codeCount** | **Integer** |  |  [optional] |
|**value** | [**CommerceDiscountValue**](CommerceDiscountValue.md) |  |  [optional] |
|**appliesTo** | [**CommerceDiscountAppliesTo**](CommerceDiscountAppliesTo.md) |  |  [optional] |
|**minimum** | [**CommerceDiscountMinimum**](CommerceDiscountMinimum.md) |  |  [optional] |
|**usageLimit** | **Integer** |  |  [optional] |
|**oncePerCustomer** | **Boolean** |  |  [optional] |
|**usageCount** | **Integer** |  |  [optional] |
|**startsAt** | **OffsetDateTime** |  |  [optional] |
|**endsAt** | **OffsetDateTime** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**platformStatus** | **String** |  |  [optional] |
|**summary** | **String** |  |  [optional] |
|**platformData** | **Map&lt;String, Object&gt;** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |



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
| BUY_X_GET_Y | &quot;buy_x_get_y&quot; |
| APP | &quot;app&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| EXPIRED | &quot;expired&quot; |



