

# UpdateGmbLocationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**selectedLocationId** | **String** |  |  |
|**googleAccountId** | **String** | Optional but recommended. The Google Business Account resource name (\&quot;accounts/123\&quot;) that owns the new location (from GET gmb-locations). When provided, the location is resolved directly instead of by enumerating the account, which is required for accounts with many locations. Named &#x60;googleAccountId&#x60; to disambiguate from the path &#x60;accountId&#x60; (the Zernio account). The legacy field name &#x60;accountId&#x60; is still accepted for backwards compatibility.  |  [optional] |
|**accountId** | **String** | Legacy alias for googleAccountId. Use googleAccountId for new integrations. |  [optional] |



