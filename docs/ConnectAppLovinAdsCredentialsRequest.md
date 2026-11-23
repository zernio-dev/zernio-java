

# ConnectAppLovinAdsCredentialsRequest

Send apiKey with eventKey, campaignApiKey with accountId, or all four. Each pair goes together (400 otherwise).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiKey** | **String** | Conversion API key from the Keys page of AppLovin Axon Ads Manager. Sent with eventKey. |  [optional] |
|**eventKey** | **String** | Event Key from the Keys page of AppLovin Axon Ads Manager: 8 to 128 letters, digits, dots, dashes or underscores. Sent with apiKey. |  [optional] |
|**campaignApiKey** | **String** | Campaign Management API key from the Keys page of ads.axon.ai (visible to account Admins only). Sent with accountId. Lets Zernio read, create and manage campaigns and creative sets. |  [optional] |
|**accountId** | **String** | Numeric AppLovin account id (Account menu, then Go to settings, in ads.axon.ai). Sent with campaignApiKey. |  [optional] |
|**reconnectAccountId** | **String** | The Zernio id of the AppLovin connection being reconnected (a connection on this profile). The keys sent update that connection, which keeps its identity, instead of creating one: send it to add or replace keys on an existing connection. |  [optional] |
|**reportKey** | **String** | Optional Report Key from the Keys page of your AppLovin account. With it, Zernio syncs AppLovin spend per campaign. |  [optional] |
|**name** | **String** | Optional display name for the account. |  [optional] |
|**profileId** | **String** | Your Zernio profile ID |  |
|**state** | **String** | Optional state passthrough for the connect flow. |  [optional] |
|**redirectUrl** | **String** | Optional URL to redirect to after a successful connection, echoed back as redirectUrl. |  [optional] |



