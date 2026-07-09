

# StartSmsRegistrationRequestBrand

Required for 10DLC. The legal entity behind the traffic (TCR brand).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) |  |  |
|**displayName** | **String** |  |  |
|**companyName** | **String** | Legal company name. Required for every entityType except SOLE_PROPRIETOR. |  [optional] |
|**ein** | **String** | Required for every entityType except SOLE_PROPRIETOR. |  [optional] |
|**phone** | **String** | Business contact phone. Required for every entityType except SOLE_PROPRIETOR. |  [optional] |
|**mobilePhone** | **String** | Required for SOLE_PROPRIETOR; the verification OTP is texted there (US/CA mobile). |  [optional] |
|**street** | **String** |  |  |
|**city** | **String** |  |  |
|**state** | **String** |  |  |
|**postalCode** | **String** |  |  |
|**country** | [**CountryEnum**](#CountryEnum) |  |  |
|**email** | **String** | Brand contact email; defaults to your account email when omitted. |  [optional] |
|**website** | **String** | The brand&#39;s website (sole proprietors may use a social profile such as LinkedIn or a business Facebook page). Carriers verify the brand against it; a bare domain is normalized to https://. |  |
|**vertical** | [**VerticalEnum**](#VerticalEnum) |  |  |
|**stockSymbol** | **String** |  |  [optional] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| PRIVATE_PROFIT | &quot;PRIVATE_PROFIT&quot; |
| PUBLIC_PROFIT | &quot;PUBLIC_PROFIT&quot; |
| NON_PROFIT | &quot;NON_PROFIT&quot; |
| GOVERNMENT | &quot;GOVERNMENT&quot; |
| SOLE_PROPRIETOR | &quot;SOLE_PROPRIETOR&quot; |



## Enum: CountryEnum

| Name | Value |
|---- | -----|
| US | &quot;US&quot; |
| CA | &quot;CA&quot; |



## Enum: VerticalEnum

| Name | Value |
|---- | -----|
| AGRICULTURE | &quot;AGRICULTURE&quot; |
| COMMUNICATION | &quot;COMMUNICATION&quot; |
| CONSTRUCTION | &quot;CONSTRUCTION&quot; |
| EDUCATION | &quot;EDUCATION&quot; |
| ENERGY | &quot;ENERGY&quot; |
| ENTERTAINMENT | &quot;ENTERTAINMENT&quot; |
| FINANCIAL | &quot;FINANCIAL&quot; |
| GAMBLING | &quot;GAMBLING&quot; |
| GOVERNMENT | &quot;GOVERNMENT&quot; |
| HEALTHCARE | &quot;HEALTHCARE&quot; |
| HOSPITALITY | &quot;HOSPITALITY&quot; |
| HUMAN_RESOURCES | &quot;HUMAN_RESOURCES&quot; |
| INSURANCE | &quot;INSURANCE&quot; |
| LEGAL | &quot;LEGAL&quot; |
| MANUFACTURING | &quot;MANUFACTURING&quot; |
| NGO | &quot;NGO&quot; |
| POLITICAL | &quot;POLITICAL&quot; |
| POSTAL | &quot;POSTAL&quot; |
| PROFESSIONAL | &quot;PROFESSIONAL&quot; |
| REAL_ESTATE | &quot;REAL_ESTATE&quot; |
| RETAIL | &quot;RETAIL&quot; |
| TECHNOLOGY | &quot;TECHNOLOGY&quot; |
| TRANSPORTATION | &quot;TRANSPORTATION&quot; |



