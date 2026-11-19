

# AdMetricRowSummary

The ad over fromDate to toDate, money in the ad account currency.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**spend** | **BigDecimal** |  |  |
|**impressions** | **BigDecimal** |  |  |
|**reach** | **BigDecimal** | Deduplicated across days for Meta ads when the platform returns it. |  |
|**clicks** | **BigDecimal** |  |  |
|**engagement** | **BigDecimal** |  |  |
|**ctr** | **BigDecimal** |  |  |
|**cpc** | **BigDecimal** |  |  |
|**cpm** | **BigDecimal** |  |  |
|**conversions** | **BigDecimal** |  |  |
|**allConversions** | **BigDecimal** |  |  |
|**costPerConversion** | **BigDecimal** |  |  |
|**actions** | **Map&lt;String, BigDecimal&gt;** |  |  |
|**actionValues** | **Map&lt;String, BigDecimal&gt;** |  |  |
|**purchaseValue** | **BigDecimal** |  |  |
|**roas** | **BigDecimal** |  |  |
|**costPerAction** | **Map&lt;String, BigDecimal&gt;** |  |  |
|**outboundClicks** | **BigDecimal** |  |  |
|**outboundClicksCtr** | **BigDecimal** |  |  |
|**inlineLinkClicks** | **BigDecimal** |  |  |
|**inlineLinkClickCtr** | **BigDecimal** |  |  |
|**uniqueClicks** | **BigDecimal** |  |  |
|**uniqueCtr** | **BigDecimal** |  |  |
|**funnel** | **Map&lt;String, BigDecimal&gt;** |  |  |
|**engagementBreakdown** | **Map&lt;String, BigDecimal&gt;** |  |  |
|**videoPlayActions** | **BigDecimal** |  |  |
|**video30SecWatchedActions** | **BigDecimal** |  |  |
|**videoThruplayWatchedActions** | **BigDecimal** |  |  |
|**videoP25WatchedActions** | **BigDecimal** |  |  |
|**videoP50WatchedActions** | **BigDecimal** |  |  |
|**videoP75WatchedActions** | **BigDecimal** |  |  |
|**videoP95WatchedActions** | **BigDecimal** |  |  |
|**videoP100WatchedActions** | **BigDecimal** |  |  |
|**videoAvgTimeWatchedActions** | **BigDecimal** |  |  |
|**video2SecWatchedActions** | **BigDecimal** |  |  |
|**video6SecWatchedActions** | **BigDecimal** |  |  |
|**video6SecFocusedViews** | **BigDecimal** |  |  |
|**costPerThruplay** | **BigDecimal** |  |  |
|**lastSyncedAt** | **String** |  |  |
|**qualityRanking** | **String** |  |  [optional] |
|**engagementRateRanking** | **String** |  |  [optional] |
|**conversionRateRanking** | **String** |  |  [optional] |
|**videoTotalWatchTime** | **BigDecimal** | Reading one ad: average watch time times plays, summed over the days. |  [optional] |



