

# ValidatePhoneNumberKycAddressRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | ISO 3166-1 alpha-2 country code. |  |
|**streetAddress** | **String** |  |  |
|**extendedAddress** | **String** | Address complement: apartment, suite, unit, or the quadra/lote used in some countries. Optional. Does not substitute for a building number on street_address. |  [optional] |
|**locality** | **String** | City / town. |  |
|**administrativeArea** | **String** | State / province / region. When omitted, the pre-check is skipped (the final submit still validates). |  [optional] |
|**postalCode** | **String** |  |  |



