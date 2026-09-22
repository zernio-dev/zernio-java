

# ConnectBlueskyCredentialsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identifier** | **String** | Your Bluesky handle (e.g. user.bsky.social) or email address |  |
|**appPassword** | **String** | App password generated from Bluesky Settings &gt; App Passwords |  |
|**state** | **String** | Required state formatted as {userId}-{profileId}. Get userId from GET /v1/users and profileId from GET /v1/profiles. |  |
|**redirectUrl** | **URI** | Optional URL to redirect to after successful connection. Used when the state carries no redirect (a state minted by GET /v1/connect/bluesky with redirect_url already carries one, and that one wins). |  [optional] |
|**redirectUri** | **URI** | Alias of redirect_url, kept for existing callers |  [optional] |



