

# SelectGoogleBusinessLocation200ResponseAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | ID of the created SocialAccount |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**username** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**selectedLocationName** | **String** | Human-readable location display name, NOT a resource name. Do not use it to build API paths. |  [optional] |
|**selectedLocationId** | **String** | Bare GBP location id. Combine with the GBP account id as accounts/{gbpAccountId}/locations/{selectedLocationId} to form the location resource names that gmb-reviews/batch expects in locationNames. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOOGLEBUSINESS | &quot;googlebusiness&quot; |



