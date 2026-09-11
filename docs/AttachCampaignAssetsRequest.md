

# AttachCampaignAssetsRequest

Provide at least one of sitelinks, callouts or structuredSnippets. Sitelink description1 and description2 must be supplied together.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio Google Ads connection id. |  |
|**customerId** | **String** | Google customer id without dashes. Required when the connection has multiple customers. |  [optional] |
|**sitelinks** | [**List&lt;GoogleSitelink&gt;**](GoogleSitelink.md) |  |  [optional] |
|**callouts** | **List&lt;String&gt;** |  |  [optional] |
|**structuredSnippets** | [**List&lt;GoogleStructuredSnippet&gt;**](GoogleStructuredSnippet.md) |  |  [optional] |



