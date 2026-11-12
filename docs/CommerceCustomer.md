

# CommerceCustomer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**phone** | **String** |  |  [optional] |
|**ordersCount** | **Integer** |  |  [optional] |
|**totalSpent** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**note** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**defaultAddress** | [**CommerceAddress**](CommerceAddress.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |
| WOOCOMMERCE | &quot;woocommerce&quot; |



