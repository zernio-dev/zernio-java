

# AdTreeAdSet

Ad set (or ad group/line item depending on platform) with rolled-up metrics and child ads

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformAdSetId** | **String** |  |  [optional] |
|**adSetName** | **String** |  |  [optional] |
|**status** | **AdStatus** | Derived from child ad statuses |  [optional] |
|**createdTime** | **OffsetDateTime** | Earliest &#x60;platformCreatedAt&#x60; (platform ad creation time; falls back to &#x60;createdAt&#x60;, Zernio&#39;s sync time, for ads synced before that field existed) across this ad set&#39;s ads. Not the ad set&#39;s own creation time on the platform — a proxy usable for sorting. |  [optional] |
|**adCount** | **Integer** |  |  [optional] |
|**budget** | [**AdTreeAdSetBudget**](AdTreeAdSetBudget.md) |  |  [optional] |
|**adSetBudget** | [**AdTreeAdSetAdSetBudget**](AdTreeAdSetAdSetBudget.md) |  |  [optional] |
|**metrics** | [**AdMetrics**](AdMetrics.md) |  |  [optional] |
|**optimizationGoal** | **String** | What the delivery system optimizes for. Meta ad set optimization goal (e.g. OFFSITE_CONVERSIONS, VALUE, LEAD_GENERATION), or on LinkedIn the campaign&#39;s effective optimizationTargetType (NONE means manual bidding). See the &#x60;optimizationGoal&#x60; field on &#x60;Ad&#x60; for the full value spaces. |  [optional] |
|**bidStrategy** | **BidStrategy** |  |  [optional] |
|**bidAmount** | **BigDecimal** | Bid amount in whole currency units. On Meta/TikTok populated when bidStrategy is LOWEST_COST_WITH_BID_CAP or COST_CAP; on LinkedIn it is the campaign&#39;s effective unitCost and pairs with &#x60;costType&#x60;, where 0 is a real, delivery-stopping value. |  [optional] |
|**roasAverageFloor** | **BigDecimal** | Minimum ROAS as a decimal multiplier (2.0 &#x3D; 2.0x). Populated when bidStrategy is LOWEST_COST_WITH_MIN_ROAS. |  [optional] |
|**costType** | **String** | LinkedIn only. Effective cost model (billing event) of the LinkedIn campaign backing this ad set: CPM, CPC or CPV. Null for non-LinkedIn ad sets. |  [optional] |
|**servingStatuses** | **List&lt;String&gt;** | LinkedIn only. Why the LinkedIn campaign backing this ad set is (or is not) delivering. A LinkedIn Campaign maps to this ad-set node, so this is the level where LinkedIn&#39;s holds actually apply. Empty means no serving data, [\&quot;RUNNABLE\&quot;] means eligible to serve, anything else is a hold. See the &#x60;servingStatuses&#x60; field on &#x60;Ad&#x60; for the known values. |  [optional] |
|**promotedObject** | [**AdTreeAdSetPromotedObject**](AdTreeAdSetPromotedObject.md) |  |  [optional] |
|**ads** | [**List&lt;Ad&gt;**](Ad.md) | Individual ads within this ad set (capped at 100). When the ad set has more than 100 ads these are the 100 highest-spending over the requested date range, so this array depends on &#x60;fromDate&#x60;/&#x60;toDate&#x60;; &#x60;adCount&#x60; is always the true ad set size. Returns a subset of Ad fields from the aggregation: &#x60;_id&#x60;, &#x60;name&#x60;, &#x60;platform&#x60;, &#x60;status&#x60;, &#x60;configuredStatus&#x60;, &#x60;reviewStatus&#x60;, &#x60;budget&#x60;, &#x60;metrics&#x60;, &#x60;creative&#x60;, &#x60;goal&#x60; and the &#x60;platform*&#x60; ids are always included; &#x60;targeting&#x60; and &#x60;schedule&#x60; may be absent. &#x60;configuredStatus&#x60; (the ad&#39;s own on/off toggle) and &#x60;reviewStatus&#x60; (the platform&#39;s review verdict) are part of this contract, not incidental: a rejected ad is only distinguishable from a healthy one through &#x60;reviewStatus&#x60;. When &#x60;timeIncrement&#x3D;1&amp;dailyLevel&#x3D;ad&#x60;, each entry also carries a &#x60;daily[]&#x60; array of &#x60;AdDailyMetrics&#x60;. |  [optional] |
|**daily** | [**List&lt;AdDailyMetrics&gt;**](AdDailyMetrics.md) | Per-day metric series for this ad set. Present only when &#x60;GET /v1/ads/tree&#x60; is called with &#x60;timeIncrement&#x3D;1&#x60; and &#x60;dailyLevel&#x60; is &#x60;adset&#x60; or &#x60;ad&#x60;. |  [optional] |



