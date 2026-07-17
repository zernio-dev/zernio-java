

# AssignGoogleBusinessLocationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Target profile to connect the location onto. |  |
|**selectedLocationId** | **String** | The Google Business location ID to assign (e.g. \&quot;locations/123\&quot;). |  |
|**googleAccountId** | **String** | Optional but recommended. The Google Business Account resource name (\&quot;accounts/123\&quot;) that owns the location (from GET gmb-locations). When provided the location is resolved directly instead of by enumerating the account, required for accounts with many locations.  |  [optional] |



