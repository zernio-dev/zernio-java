

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
|**eventNameMap** | **Map&lt;String, String&gt;** | Renames events for this destination, such as &#x60;{ \&quot;Lead\&quot;: \&quot;Purchase\&quot; }&#x60;; null sends every event under its own name. |  [optional] |
|**valueOverride** | [**ForwardingRuleValueOverride**](ForwardingRuleValueOverride.md) |  |  [optional] |
|**valueCondition** | [**ForwardingRuleValueCondition**](ForwardingRuleValueCondition.md) |  |  [optional] |
|**eventValues** | [**Map&lt;String, ForwardingRuleEventValue&gt;**](ForwardingRuleEventValue.md) | The value this destination gets for each event name, keyed by the name as received (before &#x60;eventNameMap&#x60; renames it), such as a &#x60;Lead&#x60; worth 20 EUR and a &#x60;QualifiedLead&#x60; worth 150 EUR. An event listed here ignores &#x60;valueOverride&#x60;; events not listed keep it.  The dashboard&#39;s Value sent section (Ads, Conversions, a destination) sets this map. |  [optional] |
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
| SALESFORCE | &quot;salesforce&quot; |
| GOHIGHLEVEL | &quot;gohighlevel&quot; |
| POSTBACK | &quot;postback&quot; |
| FORM_LEADS | &quot;form_leads&quot; |



