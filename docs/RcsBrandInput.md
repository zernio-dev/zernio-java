

# RcsBrandInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** |  |  |
|**legalName** | **String** | Exactly as on IRS records. |  |
|**legalEntityType** | [**LegalEntityTypeEnum**](#LegalEntityTypeEnum) |  |  |
|**organizationType** | [**OrganizationTypeEnum**](#OrganizationTypeEnum) |  |  |
|**websiteUrl** | **URI** |  |  |
|**taxId** | **String** | US: the EIN, 9 digits, optionally NN-NNNNNNN. Elsewhere: the national tax or company registration id. |  |
|**stockSymbol** | **String** | EXCHANGE:SYMBOL. Required for PUBLIC_PROFIT. |  [optional] |
|**address** | [**RcsBrandInputAddress**](RcsBrandInputAddress.md) |  |  |
|**contact** | [**RcsBrandInputContact**](RcsBrandInputContact.md) |  |  |



## Enum: LegalEntityTypeEnum

| Name | Value |
|---- | -----|
| LIMITED_LIABILITY_COMPANY | &quot;LIMITED_LIABILITY_COMPANY&quot; |
| SOLE_PROPRIETORSHIP | &quot;SOLE_PROPRIETORSHIP&quot; |
| PARTNERSHIP | &quot;PARTNERSHIP&quot; |
| CORPORATION | &quot;CORPORATION&quot; |
| S_CORPORATION | &quot;S_CORPORATION&quot; |



## Enum: OrganizationTypeEnum

| Name | Value |
|---- | -----|
| PRIVATE_PROFIT | &quot;PRIVATE_PROFIT&quot; |
| PUBLIC_PROFIT | &quot;PUBLIC_PROFIT&quot; |
| NON_PROFIT | &quot;NON_PROFIT&quot; |
| GOVERNMENT | &quot;GOVERNMENT&quot; |



