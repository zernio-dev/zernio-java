

# CreateForwardingRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**accountId** | **String** | Connected ads account ID that owns the destination. |  |
|**destinationId** | **String** | The platform destination: a pixel, a conversion action, a conversion rule, or a GA4 web stream measurement id (&#x60;G-…&#x60;). |  |
|**eventNames** | **List&lt;String&gt;** |  |  [optional] |
|**sources** | [**List&lt;SourcesEnum&gt;**](#List&lt;SourcesEnum&gt;) | Forward only events from these sources, such as only &#x60;web&#x60; for a tracked website. Leave it out to forward events from every source. |  [optional] |
|**eventNameMap** | **Map&lt;String, String&gt;** | Your event name to the name this destination gets, such as &#x60;{ \&quot;Lead\&quot;: \&quot;Purchase\&quot; }&#x60;. Names not in the map are sent unchanged.  A target spelled like a standard event in another case or form (&#x60;purchase&#x60;, &#x60;generate_lead&#x60;) is saved as the standard name (&#x60;Purchase&#x60;, &#x60;Lead&#x60;), so each platform gets its own standard event.  &#x60;eventNames&#x60; and &#x60;valueCondition&#x60; are checked against the name and value as received, before renaming. The event id is never changed, so deduplication still works. |  [optional] |
|**valueOverride** | [**ForwardingRuleValueOverride**](ForwardingRuleValueOverride.md) |  |  [optional] |
|**valueCondition** | [**ForwardingRuleValueCondition**](ForwardingRuleValueCondition.md) |  |  [optional] |
|**eventValues** | [**Map&lt;String, ForwardingRuleEventValue&gt;**](ForwardingRuleEventValue.md) | The value this destination gets for each event name, keyed by the name as received (before &#x60;eventNameMap&#x60; renames it), such as a &#x60;Lead&#x60; worth 20 EUR and a &#x60;QualifiedLead&#x60; worth 150 EUR. An event listed here ignores &#x60;valueOverride&#x60;; events not listed keep it.  The dashboard&#39;s Value sent section (Ads, Conversions, a destination) sets this map. |  [optional] |
|**apiSecret** | **String** | Google Analytics streams only: the stream&#39;s Measurement Protocol API secret (GA4 Admin › Data streams). Optional when the connection has edit access, since Zernio then creates it. Checked against Google&#39;s validation server, stored encrypted, never returned. Change it with &#x60;PATCH /v1/events/forwarding-rules/{ruleId}&#x60;. |  [optional] |



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



