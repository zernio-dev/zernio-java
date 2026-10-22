

# InstallTrackingTagOnStoreRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storeAccountId** | **String** | The connected Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) or Webflow (&#x60;webflow&#x60;) account id. |  |
|**adAccountId** | **String** | Scopes the tag lookup on platforms whose tag ids live inside an ad account. Ignored elsewhere. |  [optional] |
|**sidebarId** | **String** | WordPress only: widget area to use (see &#x60;install.preflight.sidebars&#x60; from GET). Defaults to a footer area. |  [optional] |
|**verifyHomepage** | **Boolean** | WordPress only: fetch the homepage afterwards and report &#x60;homepageCheck&#x60;. |  [optional] |



