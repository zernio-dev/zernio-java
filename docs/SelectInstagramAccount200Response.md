

# SelectInstagramAccount200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** |  |  [optional] |
|**redirectUrl** | **String** | Redirect URL if a custom redirect_url was provided. On an ads connect it also carries &#x60;adsAccountId&#x60;. |  [optional] |
|**adsAccountId** | **String** | Ads connect only (the redirect_url carries adsConnect&#x3D;true, as it does after GET /v1/connect/{platform}/ads). The metaads SocialAccount ID to use with the /v1/ads endpoints. &#x60;account.accountId&#x60; is the Instagram posting account. Absent when the ads account could not be created. |  [optional] |
|**account** | [**SelectInstagramAccount200ResponseAccount**](SelectInstagramAccount200ResponseAccount.md) |  |  [optional] |



