

# UpdateTrackingSiteRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**domains** | **List&lt;String&gt;** | Hosts allowed to send events, such as &#x60;brand.com&#x60;. Events from any other origin are dropped. |  [optional] |
|**consentMode** | **TrackingSiteConsentMode** |  |  [optional] |
|**customHostname** | **String** | A subdomain of one of the site&#39;s domains, never the domain itself. &#x60;null&#x60; removes it. |  [optional] |
|**proxyPath** | **String** | The path your server forwards to the collector, such as &#x60;/zt&#x60;. &#x60;null&#x60; removes it. |  [optional] |



