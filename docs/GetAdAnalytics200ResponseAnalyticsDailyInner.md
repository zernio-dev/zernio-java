

# GetAdAnalytics200ResponseAnalyticsDailyInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**spend** | **BigDecimal** |  |  [optional] |
|**impressions** | **Integer** |  |  [optional] |
|**reach** | **Integer** |  |  [optional] |
|**clicks** | **Integer** |  |  [optional] |
|**ctr** | **BigDecimal** | Click-through rate (%) |  [optional] |
|**cpc** | **BigDecimal** | Cost per click |  [optional] |
|**cpm** | **BigDecimal** | Cost per 1000 impressions |  [optional] |
|**engagement** | **Integer** |  |  [optional] |
|**conversions** | **Integer** | Count of conversion events matching the campaign&#39;s promoted_object.custom_event_type (PURCHASE, LEAD, etc.) over the requested date range. 0 for non-conversion campaigns or when no events have fired. Meta-only at time of writing; other platforms return 0. |  [optional] |
|**costPerConversion** | **BigDecimal** | Derived spend / conversions in the same currency as spend. 0 when conversions is 0. |  [optional] |
|**actions** | **Map&lt;String, Integer&gt;** | Raw per-action-type counts from Meta&#39;s Insights actions[] array, summed over the date range. Keys are Meta action_type strings (e.g. link_click, offsite_conversion.fb_pixel_purchase, onsite_conversion.lead_grouped). Use this to extract any conversion event (purchases, leads, add_to_cart, etc.) without relying on the derived conversions field. Empty object when no actions are reported. |  [optional] |
|**actionValues** | **Map&lt;String, BigDecimal&gt;** | Monetary mirror of &#x60;actions&#x60;, from Meta&#39;s Insights &#x60;action_values[]&#x60; array. Same keying — values are the revenue attributed to each action_type, in ad-account native currency (same unit as &#x60;spend&#x60;; see the campaign node&#39;s &#x60;currency&#x60; field). Use this to compute revenue-per-event (e.g. avg purchase value). Meta-only; other platforms return {}. |  [optional] |
|**purchaseValue** | **BigDecimal** | Convenience sum of purchase-type action values — picked from &#x60;actionValues&#x60; via the same priority list as &#x60;conversions&#x60; so both fields describe the same events. In ad-account native currency. 0 when the campaign has no purchase event configured. Meta-only. |  [optional] |
|**roas** | **BigDecimal** | Return on ad spend — derived as &#x60;purchaseValue / spend&#x60;. 0 when &#x60;spend&#x60; is 0. Equivalent to Meta&#39;s &#x60;purchase_roas&#x60; under default attribution. At ad-set and campaign levels this is recomputed from summed purchaseValue + spend (NOT averaged across children) so it&#39;s mathematically correct at every rollup level. |  [optional] |
|**lastSyncedAt** | **OffsetDateTime** | Present on individual ads only, not on campaign aggregations |  [optional] |
|**date** | **LocalDate** |  |  [optional] |



