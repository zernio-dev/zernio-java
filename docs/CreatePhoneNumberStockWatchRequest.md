

# CreatePhoneNumberStockWatchRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | ISO 3166-1 alpha-2 code of a country listed by GET /v1/phone-numbers/countries. |  |
|**numberType** | [**NumberTypeEnum**](#NumberTypeEnum) | Narrow the watch to one number type. Omit to be notified when any type in the country is back. |  [optional] |



## Enum: NumberTypeEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;local&quot; |
| MOBILE | &quot;mobile&quot; |
| NATIONAL | &quot;national&quot; |
| TOLL_FREE | &quot;toll_free&quot; |



