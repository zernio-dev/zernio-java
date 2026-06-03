

# SelectGoogleBusinessLocationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Profile ID from your connection flow |  |
|**locationId** | **String** | The Google Business location ID selected by the user |  |
|**accountId** | **String** | Optional but recommended. The Google Business Account resource name (\&quot;accounts/123\&quot;) that owns the selected location (returned per-location by GET /v1/connect/googlebusiness/locations). When provided, the location is resolved directly instead of by enumerating the account, which is required for accounts that own many locations. Omit only for small accounts.  |  [optional] |
|**pendingDataToken** | **String** | Token from the OAuth callback redirect (pendingDataToken query param). Tokens and profile data are retrieved server-side from this token. |  |
|**redirectUrl** | **URI** | Optional custom redirect URL to return to after selection |  [optional] |



