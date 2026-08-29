

# AttachCampaignAssetsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio Google Ads SocialAccount id — resolves the customer id + refresh token. |  |
|**customerId** | **String** | Numeric Google Ads customer id. Required when the connection has multiple Google Ads accounts; optional (and inferred) when it has only one. |  [optional] |
|**sitelinks** | [**List&lt;AttachCampaignAssetsRequestSitelinksInner&gt;**](AttachCampaignAssetsRequestSitelinksInner.md) | See POST /v1/ads/create sitelinks — same shape. |  [optional] |
|**callouts** | **List&lt;String&gt;** |  |  [optional] |
|**structuredSnippets** | [**List&lt;AttachCampaignAssetsRequestStructuredSnippetsInner&gt;**](AttachCampaignAssetsRequestStructuredSnippetsInner.md) |  |  [optional] |



