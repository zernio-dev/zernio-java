

# ListPhoneNumberCountries200ResponseCountriesInnerTypesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numberType** | [**NumberTypeEnum**](#NumberTypeEnum) |  |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) |  |  [optional] |
|**needsKyc** | **Boolean** |  |  [optional] |
|**monthlyCents** | **Integer** |  |  [optional] |
|**whatsappAvailable** | **Boolean** | Always false for toll_free (WhatsApp does not reliably register toll-free numbers). |  [optional] |
|**smsAvailable** | **Boolean** |  |  [optional] |
|**callsAvailable** | **Boolean** |  |  [optional] |
|**inStock** | **Boolean** |  |  [optional] |



## Enum: NumberTypeEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;local&quot; |
| MOBILE | &quot;mobile&quot; |
| NATIONAL | &quot;national&quot; |
| TOLL_FREE | &quot;toll_free&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



