

# ForwardingRule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Rule ID, used to delete it. |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**destinationId** | **String** | Platform destination (pixel, conversion action, rule, ...). |  [optional] |
|**eventNames** | **List&lt;String&gt;** | Event names forwarded to this destination; null forwards every event. |  [optional] |
|**sources** | [**List&lt;SourcesEnum&gt;**](#List&lt;SourcesEnum&gt;) | Event sources forwarded to this destination; null forwards events from every source. |  [optional] |
|**apiSecretVerified** | **Boolean** | Only when an &#x60;apiSecret&#x60; was saved by this request. Google Analytics never confirms a Measurement Protocol API secret, so it is &#x60;false&#x60; there: the first events in GA4 Realtime prove the secret is right. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: List&lt;SourcesEnum&gt;

| Name | Value |
|---- | -----|
| API | &quot;api&quot; |
| RELAY | &quot;relay&quot; |
| HUBSPOT | &quot;hubspot&quot; |
| META_LEADS | &quot;meta_leads&quot; |
| GOOGLE_LEADS | &quot;google_leads&quot; |
| LINKEDIN_LEADS | &quot;linkedin_leads&quot; |
| TIKTOK_LEADS | &quot;tiktok_leads&quot; |
| SHOPIFY | &quot;shopify&quot; |
| WOOCOMMERCE | &quot;woocommerce&quot; |
| STRIPE | &quot;stripe&quot; |
| WEB | &quot;web&quot; |



