

# AttachCampaignAssetsRequest

Provide at least one of sitelinks, callouts, structuredSnippets or images. Sitelink description1 and description2 must be supplied together.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio Google Ads connection id. |  |
|**adAccountId** | **String** | Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers. |  [optional] |
|**customerId** | **String** | Alias of adAccountId, kept for existing callers |  [optional] |
|**sitelinks** | [**List&lt;GoogleSitelink&gt;**](GoogleSitelink.md) |  |  [optional] |
|**callouts** | **List&lt;String&gt;** |  |  [optional] |
|**structuredSnippets** | [**List&lt;GoogleStructuredSnippet&gt;**](GoogleStructuredSnippet.md) |  |  [optional] |
|**images** | **List&lt;URI&gt;** | Public image URLs, uploaded to Google as image assets. Landscape 1.91:1 (min 600x314) or square 1:1 (min 300x300), up to 5 MB each. |  [optional] |



