

# ListPhoneNumberCountries200ResponseCountriesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | ISO 3166-1 alpha-2 |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) |  |  [optional] |
|**monthlyCents** | **Integer** |  |  [optional] |
|**needsKyc** | **Boolean** |  |  [optional] |
|**callsAvailable** | **Boolean** | Regular phone (PSTN) calling on the number, inbound + outbound. Available on every offerable country. |  [optional] |
|**whatsappAvailable** | **Boolean** | WhatsApp can be enabled on numbers from this country. |  [optional] |
|**smsAvailable** | **Boolean** | Whether this country&#39;s number type can do SMS. Use it to filter the picker when the buyer wants SMS (pair with &#x60;wantsSms&#x60; on purchase). |  [optional] |
|**outboundCallingAvailable** | **Boolean** | WhatsApp Business Calling (BIC) outbound availability, a Meta feature blocked in some countries. NOT the PSTN Calls feature (&#x60;callsAvailable&#x60;). |  [optional] |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



