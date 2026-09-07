

# PhoneNumberStockWatch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**country** | **String** | ISO 3166-1 alpha-2. |  |
|**countryName** | **String** |  |  |
|**numberType** | [**NumberTypeEnum**](#NumberTypeEnum) | The watched number type, or null when the watch covers every type in the country. |  |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: NumberTypeEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;local&quot; |
| MOBILE | &quot;mobile&quot; |
| NATIONAL | &quot;national&quot; |
| TOLL_FREE | &quot;toll_free&quot; |



