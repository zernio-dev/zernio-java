

# SelectSnapchatProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Your Zernio profile ID |  |
|**selectedPublicProfile** | [**SelectSnapchatProfileRequestSelectedPublicProfile**](SelectSnapchatProfileRequestSelectedPublicProfile.md) |  |  |
|**tempToken** | **String** | Temporary Snapchat access token from OAuth |  |
|**userProfile** | **Object** | User profile data from OAuth redirect |  |
|**refreshToken** | **String** | Snapchat refresh token (if available) |  [optional] |
|**expiresIn** | **Integer** | Token expiration time in seconds |  [optional] |
|**redirectUrl** | **URI** | Custom redirect URL after connection completes |  [optional] |
|**oauthAppId** | **String** | The &#x60;oauthAppId&#x60; from the selection redirect, when the connect ran on one of your own OAuth apps. Pass it back so a retried selection stays on that app; a different app than the connect used returns 400. |  [optional] |



