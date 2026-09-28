

# BrandedCallingEnterprise


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**legalName** | **String** |  |  [optional] |
|**doingBusinessAs** | **String** |  |  [optional] |
|**organizationType** | [**OrganizationTypeEnum**](#OrganizationTypeEnum) |  |  [optional] |
|**organizationLegalType** | [**OrganizationLegalTypeEnum**](#OrganizationLegalTypeEnum) |  |  [optional] |
|**countryCode** | [**CountryCodeEnum**](#CountryCodeEnum) |  |  [optional] |
|**jurisdictionOfIncorporation** | **String** |  |  [optional] |
|**website** | **String** |  |  [optional] |
|**feinLast4** | **String** | Last four digits of the tax id; the full id is never returned. |  [optional] |
|**industry** | **String** |  |  [optional] |
|**numberOfEmployees** | [**NumberOfEmployeesEnum**](#NumberOfEmployeesEnum) |  |  [optional] |
|**organizationContact** | [**BrandedCallingContact**](BrandedCallingContact.md) |  |  [optional] |
|**billingContact** | [**BrandedCallingContact**](BrandedCallingContact.md) |  |  [optional] |
|**physicalAddress** | [**BrandedCallingAddress**](BrandedCallingAddress.md) |  |  [optional] |
|**billingAddress** | [**BrandedCallingAddress**](BrandedCallingAddress.md) |  |  [optional] |
|**registered** | **Boolean** | True once the business exists at the carrier (happens when its first identity passes review). |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



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



## Enum: CountryCodeEnum

| Name | Value |
|---- | -----|
| US | &quot;US&quot; |
| CA | &quot;CA&quot; |



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



