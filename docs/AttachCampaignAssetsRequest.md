

# AttachCampaignAssetsRequest

Provide at least one of sitelinks, callouts or structuredSnippets. Sitelink description1 and description2 must be supplied together.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio Google Ads connection id. |  |
|**adAccountId** | **String** | Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers. |  [optional] |
|**customerId** | **String** | Alias of adAccountId, kept for existing callers |  [optional] |
|**sitelinks** | [**List&lt;GoogleSitelink&gt;**](GoogleSitelink.md) |  |  [optional] |
|**callouts** | **List&lt;String&gt;** |  |  [optional] |
|**structuredSnippets** | [**List&lt;GoogleStructuredSnippet&gt;**](GoogleStructuredSnippet.md) |  |  [optional] |



