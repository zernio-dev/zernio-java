

# BatchAdCatalogProductsRequestRequestsInnerProduct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**retailerId** | **String** | Your SKU; unique inside the catalog |  |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**url** | **URI** | Product page |  [optional] |
|**imageUrl** | **URI** |  |  [optional] |
|**additionalImageUrls** | **List&lt;URI&gt;** |  |  [optional] |
|**price** | **BigDecimal** | Major units, e.g. 12.99 |  [optional] |
|**currency** | **String** | ISO 4217, e.g. EUR |  [optional] |
|**salePrice** | **BigDecimal** |  |  [optional] |
|**salePriceStartDate** | **String** | ISO 8601 |  [optional] |
|**salePriceEndDate** | **String** | ISO 8601 |  [optional] |
|**availability** | [**AvailabilityEnum**](#AvailabilityEnum) |  |  [optional] |
|**condition** | [**ConditionEnum**](#ConditionEnum) |  |  [optional] |
|**brand** | **String** |  |  [optional] |
|**category** | **String** |  |  [optional] |
|**googleProductCategory** | **String** |  |  [optional] |
|**productType** | **String** |  |  [optional] |
|**gtin** | **String** |  |  [optional] |
|**mpn** | **String** |  |  [optional] |
|**inventory** | **Integer** |  |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) |  |  [optional] |
|**color** | **String** |  |  [optional] |
|**size** | **String** |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) |  |  [optional] |
|**material** | **String** |  |  [optional] |
|**pattern** | **String** |  |  [optional] |
|**customLabel0** | **String** |  |  [optional] |
|**customLabel1** | **String** |  |  [optional] |
|**customLabel2** | **String** |  |  [optional] |
|**customLabel3** | **String** |  |  [optional] |
|**customLabel4** | **String** |  |  [optional] |



## Enum: AvailabilityEnum

| Name | Value |
|---- | -----|
| IN_STOCK | &quot;in stock&quot; |
| OUT_OF_STOCK | &quot;out of stock&quot; |
| PREORDER | &quot;preorder&quot; |
| AVAILABLE_FOR_ORDER | &quot;available for order&quot; |
| DISCONTINUED | &quot;discontinued&quot; |
| PENDING | &quot;pending&quot; |



## Enum: ConditionEnum

| Name | Value |
|---- | -----|
| NEW | &quot;new&quot; |
| REFURBISHED | &quot;refurbished&quot; |
| USED | &quot;used&quot; |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| PUBLISHED | &quot;published&quot; |
| STAGING | &quot;staging&quot; |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| FEMALE | &quot;female&quot; |
| MALE | &quot;male&quot; |
| UNISEX | &quot;unisex&quot; |



