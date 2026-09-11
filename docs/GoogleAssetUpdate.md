

# GoogleAssetUpdate

Supply fields for exactly one asset type per update. finalUrls may accompany sitelinkAsset. Shared asset edits affect every attachment using the asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetResourceName** | **String** | Asset resource name returned by a list operation. Must belong to the selected customer. |  |
|**sitelinkAsset** | [**UpdateAccountSitelinksRequestUpdatesInnerSitelinkAsset**](UpdateAccountSitelinksRequestUpdatesInnerSitelinkAsset.md) |  |  [optional] |
|**finalUrls** | **List&lt;URI&gt;** |  |  [optional] |
|**calloutAsset** | [**UpdateAccountCalloutsRequestUpdatesInnerCalloutAsset**](UpdateAccountCalloutsRequestUpdatesInnerCalloutAsset.md) |  |  [optional] |
|**structuredSnippetAsset** | [**GoogleStructuredSnippet**](GoogleStructuredSnippet.md) |  |  [optional] |



