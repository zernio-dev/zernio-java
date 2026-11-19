

# AdLeadAttribution

`web` leads only: where the lead came from. Its stage events (`QualifiedLead`, `Purchase`) carry these so the ad platforms can match them. Null for ad network leads.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clickIds** | **Map&lt;String, String&gt;** | Ad click and browser ids of the visit (&#x60;fbc&#x60;, &#x60;fbp&#x60;, &#x60;gclid&#x60;, &#x60;ttclid&#x60;, ...). |  [optional] |
|**utm** | **Map&lt;String, String&gt;** |  |  [optional] |
|**visitorId** | **String** | The Zernio tag visitor id (&#x60;_zid&#x60;). |  [optional] |
|**sourceUrl** | **String** | The page the form was submitted on. |  [optional] |
|**siteId** | **String** | The tracked website, for a website form lead. |  [optional] |



