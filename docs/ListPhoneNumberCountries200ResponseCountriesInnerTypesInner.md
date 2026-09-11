

# ListPhoneNumberCountries200ResponseCountriesInnerTypesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numberType** | [**NumberTypeEnum**](#NumberTypeEnum) |  |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | Null on a &#x60;fulfilment: request&#x60; type, whose document tier is only known once its requirements are read. |  [optional] |
|**needsKyc** | **Boolean** |  |  [optional] |
|**monthlyCents** | **Integer** | Price a NEW number of this type costs per month, in cents. |  [optional] |
|**whatsappAvailable** | **Boolean** | Always false for toll_free (WhatsApp does not reliably register toll-free numbers). |  [optional] |
|**smsAvailable** | **Boolean** |  |  [optional] |
|**callsAvailable** | **Boolean** |  |  [optional] |
|**inStock** | **Boolean** |  |  [optional] |
|**fulfilment** | [**FulfilmentEnum**](#FulfilmentEnum) | &#x60;request&#x60;: the carrier stocks this type nowhere and only sources it to order, so it is always a pre-order. |  [optional] |
|**preOrderable** | **Boolean** | Out of stock but orderable anyway. Submit KYC as usual (POST /v1/phone-numbers/kyc): we buy regular stock the moment it returns, otherwise the carrier sources the number. Usually 2 to 4 weeks, never guaranteed. Only document tiers (3/4) qualify, and nothing is billed until the number is active. |  [optional] |



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



## Enum: FulfilmentEnum

| Name | Value |
|---- | -----|
| INSTANT | &quot;instant&quot; |
| REQUEST | &quot;request&quot; |



