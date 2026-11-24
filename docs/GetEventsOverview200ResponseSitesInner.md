

# GetEventsOverview200ResponseSitesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**siteId** | **String** |  |  [optional] |
|**profileId** | **String** | The profile the site belongs to. |  [optional] |
|**hitsToday** | **Integer** | Hits today. |  [optional] |
|**lastActiveOn** | **LocalDate** | The last day in the past 7 with a hit. &#x60;null&#x60; when none. |  [optional] |
|**eventNamesLastWeek** | **List&lt;String&gt;** | Each event name people (not bots) sent the site in the last 7 days, sorted. Names the site sends that are neither standard nor in its &#x60;customEvents&#x60; are left out. |  [optional] |
|**totals** | [**GetEventsOverview200ResponseSitesInnerTotals**](GetEventsOverview200ResponseSitesInnerTotals.md) |  |  [optional] |



