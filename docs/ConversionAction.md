

# ConversionAction

A Google Ads conversion action, e.g. a WEBPAGE conversion created via `createConversionAction`. Returned by `listConversionActions` and `createConversionAction`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Google Ads conversion action id. |  |
|**name** | **String** |  |  |
|**type** | **String** | Google&#39;s ConversionActionType, e.g. WEBPAGE, UPLOAD_CLICKS. |  |
|**status** | **String** | Google&#39;s ConversionActionStatus, e.g. ENABLED, REMOVED, HIDDEN. |  |
|**category** | **String** | Google&#39;s ConversionActionCategory, e.g. DEFAULT, PURCHASE, LEAD. |  |
|**tagSnippets** | [**List&lt;ConversionActionTagSnippetsInner&gt;**](ConversionActionTagSnippetsInner.md) | The code a customer pastes onto their site. Present for types Google generates a snippet for (e.g. WEBPAGE); empty otherwise.  |  |



