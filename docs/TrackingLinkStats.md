

# TrackingLinkStats


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromDate** | **LocalDate** |  |  |
|**toDate** | **LocalDate** |  |  |
|**clicks** | **Integer** | Human clicks in the range. |  |
|**conversions** | **Integer** | Conversions still counted whose time falls in the range. |  |
|**conversionRate** | **BigDecimal** | Conversions per click. Null without clicks. |  |
|**revenue** | [**List&lt;TrackingLinkStatsRevenueInner&gt;**](TrackingLinkStatsRevenueInner.md) | The conversions&#39; value summed per currency, most conversions first. |  |
|**destinations** | [**List&lt;TrackingLinkStatsDestinationsInner&gt;**](TrackingLinkStatsDestinationsInner.md) | The link&#39;s current destinations, each with its clicks in the range. |  |
|**formerDestinationClicks** | **Integer** | Clicks on destinations the link no longer has (an edited or removed URL). |  |



