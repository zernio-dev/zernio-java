

# AdsPerformanceResponseAdsInnerMetrics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**spend** | **BigDecimal** | In the ad&#39;s currency. |  [optional] |
|**impressions** | **Integer** |  |  [optional] |
|**reach** | **Integer** | People who saw the ad. De-duplicated over the range on Meta and TikTok when the platform returns it; elsewhere the sum of each day&#39;s reach, which counts a person once per day. |  [optional] |
|**frequency** | **BigDecimal** | Average times each person saw the ad: &#x60;impressions / reach&#x60;. 0 when the platform reports no reach. |  [optional] |
|**clicks** | **Integer** |  |  [optional] |
|**ctr** | **BigDecimal** | Percent. |  [optional] |
|**conversions** | **BigDecimal** | Results over the range (see AdMetrics.conversions). |  [optional] |
|**costPerConversion** | **BigDecimal** |  |  [optional] |
|**purchaseValue** | **BigDecimal** |  |  [optional] |
|**roas** | **BigDecimal** |  |  [optional] |
|**conversionsByType** | **Map&lt;String, BigDecimal&gt;** | &#x60;conversions&#x60; split by what was counted (Meta action_type or Google conversion action name). |  [optional] |



