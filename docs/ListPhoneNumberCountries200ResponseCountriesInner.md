

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
|**inStock** | **Boolean** | Live carrier-stock snapshot (refreshed every 6h + on availability checks): false when NO offered type currently has deliverable inventory, so a purchase would fail. Treat as advisory; the purchase itself re-checks. |  [optional] |
|**types** | [**List&lt;ListPhoneNumberCountries200ResponseCountriesInnerTypesInner&gt;**](ListPhoneNumberCountries200ResponseCountriesInnerTypesInner.md) | Every number type offered in this country (default first). Capabilities, KYC tier, monthly price, and stock are per type. The country-level fields above mirror the first (default) entry. Pass the chosen &#x60;numberType&#x60; to POST /v1/phone-numbers/purchase.  |  [optional] |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



