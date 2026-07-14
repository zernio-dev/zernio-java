

# CreatePhoneNumberPortInRequestEndUser

End-user / current-carrier account info that authorizes the port. The losing carrier matches every field against its records and rejects the whole port on a mismatch — enter values exactly as they appear on the carrier bill. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityName** | **String** | Account holder / business name, as on the carrier account. |  |
|**authPersonName** | **String** | Full name (first + last) of the person authorizing the port — must match the LOA signature. |  |
|**billingPhoneNumber** | **String** | Phone number on the losing carrier&#39;s bill. Defaults to the ported number itself on single-number orders. Validated as a real phone number when present. |  [optional] |
|**accountNumber** | **String** | Account number with the losing carrier — required (carriers reject ports without it; on prepaid mobile plans it is often the phone number itself). |  |
|**pinPasscode** | **String** | Transfer PIN. Required for mobile numbers (wireless carriers reject PIN-less ports). Forwarded to the carrier, never stored. |  [optional] |
|**streetAddress** | **String** |  |  |
|**extendedAddress** | **String** |  |  [optional] |
|**locality** | **String** |  |  |
|**administrativeArea** | **String** | 2-letter US state / CA province code (full names are accepted and normalized). |  |
|**postalCode** | **String** | US ZIP (5 digits) or Canadian postal code, matching countryCode. |  |
|**countryCode** | [**CountryCodeEnum**](#CountryCodeEnum) |  |  |



## Enum: CountryCodeEnum

| Name | Value |
|---- | -----|
| US | &quot;US&quot; |
| CA | &quot;CA&quot; |



