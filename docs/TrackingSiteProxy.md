

# TrackingSiteProxy

The path your server forwards to the collector, so the tag runs from the site's own domain. Null when it has none.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**path** | **String** | Such as &#x60;/zt&#x60;: the snippet loads &#x60;https://&lt;first domain&gt;/zt/z.js&#x60;. |  [optional] |
|**secret** | **String** | Signs the visitor&#39;s IP and country your proxy forwards. Only on reading or updating one site. |  [optional] |
|**googleTags** | [**List&lt;TrackingSiteProxyGoogleTagsInner&gt;**](TrackingSiteProxyGoogleTagsInner.md) | The loader of each of &#x60;googleTagIds&#x60; on the site&#39;s own domain. Use &#x60;src&#x60; in place of the tag&#39;s googletagmanager.com address. |  [optional] |



