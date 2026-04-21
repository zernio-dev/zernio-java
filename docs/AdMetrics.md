

# AdMetrics


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
|**lastSyncedAt** | **OffsetDateTime** | Present on individual ads only, not on campaign aggregations |  [optional] |



