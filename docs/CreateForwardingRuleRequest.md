

# CreateForwardingRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**accountId** | **String** | Connected ads account ID that owns the destination. |  |
|**destinationId** | **String** | The platform destination: a pixel, a conversion action or a conversion rule. |  |
|**eventNames** | **List&lt;String&gt;** |  |  [optional] |
|**sources** | [**List&lt;SourcesEnum&gt;**](#List&lt;SourcesEnum&gt;) | Forward only events from these sources, such as only &#x60;web&#x60; for a tracked website. Leave it out to forward events from every source. |  [optional] |



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



