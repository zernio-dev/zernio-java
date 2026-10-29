

# AdTreeAdSet

Ad set (or ad group/line item depending on platform) with rolled-up metrics and child ads

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformAdSetId** | **String** |  |  [optional] |
|**adSetName** | **String** |  |  [optional] |
|**status** | **AdStatus** | Derived from child ad statuses |  [optional] |
|**createdTime** | **OffsetDateTime** | Earliest &#x60;platformCreatedAt&#x60; (platform ad creation time; falls back to &#x60;createdAt&#x60;, Zernio&#39;s sync time, for ads synced before that field existed) across this ad set&#39;s ads. Not the ad set&#39;s own creation time on the platform, but a proxy usable for sorting. |  [optional] |
|**adCount** | **Integer** |  |  [optional] |
|**isSmartPlus** | **Boolean** | TikTok only. true when this ad group belongs to an Upgraded Smart+ campaign. See AdTreeCampaign.isSmartPlus. |  [optional] |
|**budget** | [**AdTreeAdSetBudget**](AdTreeAdSetBudget.md) |  |  [optional] |
|**adSetBudget** | [**AdTreeAdSetAdSetBudget**](AdTreeAdSetAdSetBudget.md) |  |  [optional] |
|**metrics** | [**AdMetrics**](AdMetrics.md) |  |  [optional] |
|**previousMetrics** | [**AdMetrics**](AdMetrics.md) | Only with &#x60;compare&#x3D;previous&#x60;. The same metrics over &#x60;previousRange&#x60;. |  [optional] |
|**optimizationGoal** | **String** | What the delivery system optimizes for. Meta ad set optimization goal (e.g. OFFSITE_CONVERSIONS, VALUE, LEAD_GENERATION), or on LinkedIn the campaign&#39;s effective optimizationTargetType (NONE means manual bidding). See the &#x60;optimizationGoal&#x60; field on &#x60;Ad&#x60; for the full value spaces. |  [optional] |
|**bidStrategy** | **BidStrategy** |  |  [optional] |
|**bidAmount** | **BigDecimal** | Bid amount in whole currency units. On Meta/TikTok populated when bidStrategy is LOWEST_COST_WITH_BID_CAP or COST_CAP; on LinkedIn it is the campaign&#39;s effective unitCost and pairs with &#x60;costType&#x60;, where 0 is a real, delivery-stopping value. |  [optional] |
|**roasAverageFloor** | **BigDecimal** | Minimum ROAS as a decimal multiplier (2.0 &#x3D; 2.0x). Populated when bidStrategy is LOWEST_COST_WITH_MIN_ROAS. |  [optional] |
|**costType** | **String** | LinkedIn only. Effective cost model (billing event) of the LinkedIn campaign backing this ad set: CPM, CPC or CPV. Null for non-LinkedIn ad sets. |  [optional] |
|**servingStatuses** | **List&lt;String&gt;** | LinkedIn only. Why the LinkedIn campaign backing this ad set is (or is not) delivering. A LinkedIn Campaign maps to this ad-set node, so this is the level where LinkedIn&#39;s holds apply.  - Empty: no serving data. - [\&quot;RUNNABLE\&quot;]: eligible to serve. - Anything else: a hold. See the &#x60;servingStatuses&#x60; field on &#x60;Ad&#x60; for the known values.  |  [optional] |
|**learningStatus** | [**LearningStatusEnum**](#LearningStatusEnum) | Meta only. Where the ad set stands in Meta&#39;s learning phase, as of the last sync. Null on other platforms and for ad sets not yet synced.  - LEARNING: delivery is still being optimized (about 50 optimization events in 7 days end it). - SUCCESS: it has left learning. - FAIL: it could not gather enough events (Ads Manager&#39;s \&quot;Learning limited\&quot;).  |  [optional] |
|**promotedObject** | [**AdTreeAdSetPromotedObject**](AdTreeAdSetPromotedObject.md) |  |  [optional] |
|**destinationType** | **String** | Meta only. Where the ad set sends people (Meta &#x60;destination_type&#x60;), e.g. WEBSITE, MESSENGER, WHATSAPP, INSTAGRAM_DIRECT, ON_AD. Meta answers UNDEFINED for an ad set with no explicit destination. As of the last sync; null on other platforms and for ad sets not yet synced. |  [optional] |
|**attributionSpec** | [**List&lt;AdTreeAdSetAttributionSpecInner&gt;**](AdTreeAdSetAttributionSpecInner.md) | Meta only. The ad set&#39;s conversion attribution windows (Meta &#x60;attribution_spec&#x60;), in the same shape &#x60;attributionSpec&#x60; takes on ad creation so a clone can send it back unchanged. As of the last sync; null on other platforms, for ad sets not yet synced and when Meta reports none. |  [optional] |
|**regionalRegulatedCategories** | **List&lt;String&gt;** | Meta only. Regional regulated categories declared on the ad set (Meta &#x60;regional_regulated_categories&#x60;), e.g. AUSTRALIA_FINSERV, TAIWAN_UNIVERSAL, SINGAPORE_UNIVERSAL or VOLUNTARY_VERIFICATION. As of the last sync; null on other platforms, for ad sets not yet synced and when Meta reports none. |  [optional] |
|**regionalRegulationIdentities** | **Map&lt;String, String&gt;** | Meta only. Verified identity IDs per regional regulation role (Meta &#x60;regional_regulation_identities&#x60;), keyed by Meta&#39;s role name. IDs are strings because they can exceed a JSON number&#39;s precision. As of the last sync; null on other platforms, for ad sets not yet synced and when Meta reports none. |  [optional] |
|**ads** | [**List&lt;Ad&gt;**](Ad.md) | Individual ads within this ad set (capped at 100). With more than 100 ads these are the 100 highest-spending over the requested date range, so the array depends on &#x60;fromDate&#x60;/&#x60;toDate&#x60;. &#x60;adCount&#x60; is always the true ad set size.  A subset of Ad fields from the aggregation. Always included: &#x60;_id&#x60;, &#x60;name&#x60;, &#x60;platform&#x60;, &#x60;status&#x60;, &#x60;configuredStatus&#x60;, &#x60;reviewStatus&#x60;, &#x60;budget&#x60;, &#x60;metrics&#x60;, &#x60;creative&#x60;, &#x60;goal&#x60; and the &#x60;platform*&#x60; ids. &#x60;targeting&#x60; and &#x60;schedule&#x60; may be absent.  &#x60;configuredStatus&#x60; (the ad&#39;s own on/off toggle) and &#x60;reviewStatus&#x60; (the platform&#39;s review verdict) are part of this contract, not incidental: only &#x60;reviewStatus&#x60; distinguishes a rejected ad from a healthy one.  When &#x60;timeIncrement&#x3D;1&amp;dailyLevel&#x3D;ad&#x60;, each entry also carries a &#x60;daily[]&#x60; array of &#x60;AdDailyMetrics&#x60;.  |  [optional] |
|**daily** | [**List&lt;AdDailyMetrics&gt;**](AdDailyMetrics.md) | Per-day metric series for this ad set. Present only when &#x60;GET /v1/ads/tree&#x60; is called with &#x60;timeIncrement&#x3D;1&#x60; and &#x60;dailyLevel&#x60; is &#x60;adset&#x60; or &#x60;ad&#x60;. |  [optional] |



## Enum: LearningStatusEnum

| Name | Value |
|---- | -----|
| LEARNING | &quot;LEARNING&quot; |
| SUCCESS | &quot;SUCCESS&quot; |
| FAIL | &quot;FAIL&quot; |



