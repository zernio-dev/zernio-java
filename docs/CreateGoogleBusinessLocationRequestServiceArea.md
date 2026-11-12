

# CreateGoogleBusinessLocationRequestServiceArea

Areas the business serves. Required unless storefrontAddress is provided.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**businessType** | [**BusinessTypeEnum**](#BusinessTypeEnum) |  |  |
|**regionCode** | **String** | Required when businessType is CUSTOMER_LOCATION_ONLY. |  [optional] |
|**places** | [**CreateGoogleBusinessLocationRequestServiceAreaPlaces**](CreateGoogleBusinessLocationRequestServiceAreaPlaces.md) |  |  [optional] |



## Enum: BusinessTypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_LOCATION_ONLY | &quot;CUSTOMER_LOCATION_ONLY&quot; |
| CUSTOMER_AND_BUSINESS_LOCATION | &quot;CUSTOMER_AND_BUSINESS_LOCATION&quot; |



