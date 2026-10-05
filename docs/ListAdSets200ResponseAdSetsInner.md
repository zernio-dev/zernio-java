

# ListAdSets200ResponseAdSetsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformAdSetId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**adSetName** | **String** |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**platformAdSetStatus** | **String** | Raw platform ad set status. On TikTok the ad group&#39;s own switch &#x60;operation_status&#x60; (ENABLE / DISABLE), independent of its campaign. |  [optional] |
|**platformCampaignId** | **String** |  |  [optional] |
|**platformAdAccountId** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**budget** | [**ListAdSets200ResponseAdSetsInnerBudget**](ListAdSets200ResponseAdSetsInnerBudget.md) |  |  [optional] |
|**schedule** | [**ListAdSets200ResponseAdSetsInnerSchedule**](ListAdSets200ResponseAdSetsInnerSchedule.md) |  |  [optional] |
|**targeting** | **ListAdSets200ResponseAdSetsInnerTargeting** |  |  [optional] |
|**isExternal** | **Boolean** |  |  [optional] |
|**platformCreatedAt** | **OffsetDateTime** |  |  [optional] |
|**statusReadAt** | **OffsetDateTime** | Only with &#x60;live&#x3D;true&#x60;. When &#x60;platformAdSetStatus&#x60; was read from the platform; null when this row was not read live. |  [optional] |
|**optimizationGoal** | **String** | The ad set&#39;s optimization goal as last synced, in the platform&#39;s own enum (Meta &#x60;optimization_goal&#x60;, for example OFFSITE_CONVERSIONS or LINK_CLICKS). On TikTok with &#x60;live&#x3D;true&#x60;, rows read live carry the ad group&#39;s &#x60;optimization_goal&#x60; exactly as TikTok&#39;s adgroup/get returns it now (for example ENGAGED_VIEW, ENGAGED_VIEW_FIFTEEN, CLICK, CONVERT). |  [optional] |
|**billingEvent** | **String** | The ad set&#39;s billing event as last synced, where the platform reports one. On TikTok with &#x60;live&#x3D;true&#x60;, rows read live carry the ad group&#39;s &#x60;billing_event&#x60; exactly as TikTok&#39;s adgroup/get returns it now (for example CPV, CPC, OCPM). |  [optional] |
|**bidStrategy** | **String** | The bid strategy as last synced, in the platform&#39;s own enum (Meta &#x60;bid_strategy&#x60;, for example LOWEST_COST_WITHOUT_CAP, COST_CAP). On Meta under a campaign budget this is the campaign&#39;s strategy. |  [optional] |
|**bidAmount** | **BigDecimal** | Bid cap or cost target in whole units of &#x60;currency&#x60;, as last synced. Null when the strategy has none. |  [optional] |
|**promotedObject** | **Map&lt;String, Object&gt;** | Meta only. The ad set&#39;s &#x60;promoted_object&#x60; verbatim (snake_case, for example pixel_id + custom_event_type, page_id, application_id), as last synced from its most recent ad. Null on other platforms and on an ad set with no ad yet; GET /v1/ads/accounts/live reads it live for every ad set. |  [optional] |
|**nativeSettings** | **Map&lt;String, Object&gt;** | TikTok only, only with &#x60;live&#x3D;true&#x60; and only on rows read live. TikTok&#39;s adgroup/get record verbatim (snake_case, TikTok&#39;s own names and enums): operation_status, optimization_goal, optimization_event, billing_event, bid_type, bid_price, budget, budget_mode, pacing, schedule_type, schedule_start_time, schedule_end_time, dayparting, placement_type, placements, location_ids, age_groups, gender, languages, interest_category_ids, interest_keyword_ids, actions, audience_ids, excluded_audience_ids, operating_systems, frequency, frequency_schedule, smart_audience_enabled, smart_interest_behavior_enabled. schedule_start_time and schedule_end_time are UTC wall clocks (YYYY-MM-DD HH:MM:SS). location_ids holds TikTok&#39;s native location ids (GeoNames ids for countries); GET /v1/ads/targeting/search?dimension&#x3D;geo returns them as &#x60;platformId&#x60; on country results. Plus advertiser_currency and advertiser_timezone from TikTok&#39;s advertiser/info. A field TikTok does not return is absent. |  [optional] |
|**configReadAt** | **OffsetDateTime** | Only with &#x60;live&#x3D;true&#x60;. When &#x60;nativeSettings&#x60; was read from the platform. Null on every row whose native settings were not read now (row past the cap, failed read, or a platform without a native read). |  [optional] |



