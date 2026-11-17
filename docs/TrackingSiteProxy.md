

# TrackingSiteProxy

The path your server forwards to the collector, so the tag runs from the site's own domain. Null when it has none.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**path** | **String** | Such as &#x60;/zt&#x60;: the snippet loads &#x60;https://&lt;first domain&gt;/zt/z.js&#x60;. |  [optional] |
|**secret** | **String** | Signs the visitor&#39;s IP and country your proxy forwards. Only on reading or updating one site. |  [optional] |



