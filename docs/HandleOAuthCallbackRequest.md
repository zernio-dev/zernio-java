

# HandleOAuthCallbackRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** |  |  |
|**state** | **String** | For twitter, the state X returned on the redirect (the same as the state query parameter of authUrl, ending in its -cv_ PKCE verifier suffix), signed and under 1 hour old. The state field of the GET JSON response does not carry the verifier. |  |
|**profileId** | **String** |  |  |



