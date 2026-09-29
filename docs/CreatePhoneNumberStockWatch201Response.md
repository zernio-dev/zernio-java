

# CreatePhoneNumberStockWatch201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**country** | **String** | ISO 3166-1 alpha-2. |  |
|**countryName** | **String** |  |  |
|**numberType** | [**NumberTypeEnum**](#NumberTypeEnum) | The watched number type, or null when the watch covers every type in the country. |  |
|**areaCode** | **String** | The watched area code (NDC), or null when the watch covers every area. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**preOrderable** | **Boolean** | True when the watched area can be bought today as a pre-order (the carrier lists nothing there and the type is a document tier): submit KYC with &#x60;areaCode&#x60; and &#x60;preOrder: true&#x60; instead of waiting, usually 2 to 4 weeks, nothing billed until active. The watch is armed either way. |  [optional] |



## Enum: NumberTypeEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;local&quot; |
| MOBILE | &quot;mobile&quot; |
| NATIONAL | &quot;national&quot; |
| TOLL_FREE | &quot;toll_free&quot; |



