

# CreatePhoneNumberPortInRequestEndUser

End-user / current-carrier account info that authorizes the port. The losing carrier matches every field against its records and rejects the whole port on a mismatch — enter values exactly as they appear on the carrier bill. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityName** | **String** | Account holder / business name, as on the carrier account. |  |
|**authPersonName** | **String** | Full name (first + last) of the person authorizing the port — must match the LOA signature. |  |
|**billingPhoneNumber** | **String** | Phone number on the losing carrier&#39;s bill. Defaults to the ported number itself on single-number orders. Validated as a real phone number when present. |  [optional] |
|**accountNumber** | **String** | Account number with the losing carrier — required (carriers reject ports without it; on prepaid mobile plans it is often the phone number itself). |  |
|**pinPasscode** | **String** | Transfer PIN. Required for US/CA mobile numbers (wireless carriers reject PIN-less ports). Forwarded to the carrier, never stored. International porting codes (e.g. the UK PAC) go through &#x60;requirements&#x60; instead. |  [optional] |
|**taxIdentifier** | **String** | Company tax id on the carrier account (EU ports, e.g. Spanish CIF). |  [optional] |
|**businessIdentifier** | **String** | Business registration id on the carrier account (EU ports). |  [optional] |
|**streetAddress** | **String** |  |  |
|**extendedAddress** | **String** |  |  [optional] |
|**locality** | **String** |  |  |
|**administrativeArea** | **String** | Region. Required for US/CA as the 2-letter state/province code (full names are accepted and normalized); optional elsewhere. |  [optional] |
|**postalCode** | **String** | Postal code. Validated as a US ZIP / Canadian postal code for US/CA; free-form elsewhere. |  |
|**countryCode** | [**CountryCodeEnum**](#CountryCodeEnum) | Service-address country (a supported port-in country). |  |



## Enum: CountryCodeEnum

| Name | Value |
|---- | -----|
| US | &quot;US&quot; |
| CA | &quot;CA&quot; |
| GB | &quot;GB&quot; |
| ES | &quot;ES&quot; |
| DE | &quot;DE&quot; |
| FR | &quot;FR&quot; |
| NL | &quot;NL&quot; |
| AU | &quot;AU&quot; |



