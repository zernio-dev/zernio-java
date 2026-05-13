

# GetAdsTimeline200ResponseRowsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **LocalDate** |  |  [optional] |
|**spend** | **BigDecimal** | Native currency units (matches /ads/tree convention). |  [optional] |
|**impressions** | **Integer** |  |  [optional] |
|**reach** | **Integer** |  |  [optional] |
|**clicks** | **Integer** |  |  [optional] |
|**engagement** | **Integer** |  |  [optional] |
|**ctr** | **BigDecimal** | Click-through rate as a percentage (0–100). |  [optional] |
|**cpc** | **BigDecimal** | Cost per click in native currency. |  [optional] |
|**cpm** | **BigDecimal** | Cost per 1000 impressions in native currency. |  [optional] |
|**conversions** | **Integer** | Sum of conversion events matching the campaign optimization goal. Meta-only at time of writing. |  [optional] |
|**costPerConversion** | **BigDecimal** |  |  [optional] |
|**actions** | **Map&lt;String, BigDecimal&gt;** | Per-action-type counts merged across all ads on this day. Keys are platform-native action types. |  [optional] |
|**actionValues** | **Map&lt;String, BigDecimal&gt;** | Monetary mirror of &#x60;actions&#x60; in native currency. |  [optional] |
|**purchaseValue** | **BigDecimal** | Sum of purchase-type action values on this day, native currency. |  [optional] |
|**roas** | **BigDecimal** | Derived purchaseValue / spend. |  [optional] |



