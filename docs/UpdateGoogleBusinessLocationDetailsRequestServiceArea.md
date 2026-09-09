

# UpdateGoogleBusinessLocationDetailsRequestServiceArea

Areas the business serves. Use updateMask='serviceArea'. Full replacement: send every place you want to keep.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**businessType** | [**BusinessTypeEnum**](#BusinessTypeEnum) |  |  [optional] |
|**places** | [**UpdateGoogleBusinessLocationDetailsRequestServiceAreaPlaces**](UpdateGoogleBusinessLocationDetailsRequestServiceAreaPlaces.md) |  |  [optional] |
|**regionCode** | **String** | Immutable. CLDR region code of the country the business is based in (e.g. &#39;BR&#39;) |  [optional] |



## Enum: BusinessTypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_LOCATION_ONLY | &quot;CUSTOMER_LOCATION_ONLY&quot; |
| CUSTOMER_AND_BUSINESS_LOCATION | &quot;CUSTOMER_AND_BUSINESS_LOCATION&quot; |



