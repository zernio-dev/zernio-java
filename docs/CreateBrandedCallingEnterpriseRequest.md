

# CreateBrandedCallingEnterpriseRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**legalName** | **String** | Exactly as on the tax record. |  |
|**doingBusinessAs** | **String** |  |  |
|**organizationType** | [**OrganizationTypeEnum**](#OrganizationTypeEnum) |  |  |
|**organizationLegalType** | [**OrganizationLegalTypeEnum**](#OrganizationLegalTypeEnum) |  |  |
|**countryCode** | **String** | ISO 3166-1 alpha-2. US or CA. |  |
|**jurisdictionOfIncorporation** | **String** | State, province or country of registration. |  |
|**website** | **URI** |  |  |
|**fein** | **String** | US Federal Employer Identification Number (NN-NNNNNNN) or the Canadian equivalent. Stored encrypted; only the last four digits are ever returned. |  |
|**industry** | **String** | One of the carrier industry labels, e.g. technology, healthcare, retail, finance, legal, insurance, real estate, logistics, education. |  |
|**numberOfEmployees** | [**NumberOfEmployeesEnum**](#NumberOfEmployeesEnum) |  |  |
|**organizationContact** | [**BrandedCallingContact**](BrandedCallingContact.md) |  |  |
|**billingContact** | [**BrandedCallingContact**](BrandedCallingContact.md) |  |  |
|**physicalAddress** | [**BrandedCallingAddress**](BrandedCallingAddress.md) |  |  |
|**billingAddress** | [**BrandedCallingAddress**](BrandedCallingAddress.md) |  |  |



## Enum: OrganizationTypeEnum

| Name | Value |
|---- | -----|
| COMMERCIAL | &quot;commercial&quot; |
| GOVERNMENT | &quot;government&quot; |
| NON_PROFIT | &quot;non_profit&quot; |



## Enum: OrganizationLegalTypeEnum

| Name | Value |
|---- | -----|
| CORPORATION | &quot;corporation&quot; |
| LLC | &quot;llc&quot; |
| PARTNERSHIP | &quot;partnership&quot; |
| NONPROFIT | &quot;nonprofit&quot; |
| OTHER | &quot;other&quot; |



## Enum: NumberOfEmployeesEnum

| Name | Value |
|---- | -----|
| _1_10 | &quot;1-10&quot; |
| _11_50 | &quot;11-50&quot; |
| _51_200 | &quot;51-200&quot; |
| _201_500 | &quot;201-500&quot; |
| _501_2000 | &quot;501-2000&quot; |
| _2001_10000 | &quot;2001-10000&quot; |
| _10001_ | &quot;10001+&quot; |



