

# UpdateAdSetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**budget** | [**UpdateAdSetRequestBudget**](UpdateAdSetRequestBudget.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Omit if not toggling delivery state |  [optional] |
|**name** | **String** | Rename the ad set (Meta only; other platforms return 501). At least one of budget/status/bidStrategy/name is required. |  [optional] |
|**bidStrategy** | **BidStrategy** | Ad-set-level bid strategy. Overrides the campaign-level default. Supported on Meta (facebook, instagram), TikTok, and OpenAI. On TikTok the Meta-style enum is mapped to bid_type / bid_price / deep_bid_type automatically. On OpenAI, LOWEST_COST_WITH_BID_CAP and COST_CAP both map to the ad group&#39;s &#x60;bidding_config.max_bid_micros&#x60; (one knob covers both); LOWEST_COST_WITH_MIN_ROAS is rejected with 422 (OpenAI has no ROAS-based bidding). Other platforms (linkedin, pinterest, google, twitter) return 501 Not Implemented when bidStrategy is set.  |  [optional] |
|**bidAmount** | **BigDecimal** | Bid cap in WHOLE currency units (USD: 5 &#x3D; $5.00; JPY: 100 &#x3D; ¥100). Required when bidStrategy is LOWEST_COST_WITH_BID_CAP or COST_CAP. Internally converted to Meta&#39;s smallest-denomination integer, or (on OpenAI) to micros (× 1,000,000).  |  [optional] |
|**roasAverageFloor** | **BigDecimal** | Minimum ROAS as a decimal multiplier (2.0 &#x3D; 2.0x). Required when bidStrategy is LOWEST_COST_WITH_MIN_ROAS. Sent to Meta as &#x60;bid_constraints.roas_average_floor&#x60; × 10000. Not supported on OpenAI (422).  |  [optional] |
|**valueRuleSetId** | **String** | Meta only (other platforms return 501). Value rule set to attach to this ad set, from &#x60;/v1/ads/value-rule-sets&#x60;. Sending a different id replaces the current association. To DETACH, send &#x60;valueRulesApplied: false&#x60; and omit this field.  |  [optional] |
|**valueRulesApplied** | **Boolean** | Meta only (other platforms return 501). &#x60;false&#x60; DETACHES the ad set&#39;s value rule set and must be sent WITHOUT &#x60;valueRuleSetId&#x60;; the combination returns 400. &#x60;true&#x60; is optional when attaching, since attachment is driven by &#x60;valueRuleSetId&#x60;, and requires it to be present.  |  [optional] |
|**platformSpecificData** | [**UpdateAdSetRequestPlatformSpecificData**](UpdateAdSetRequestPlatformSpecificData.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| TIKTOK | &quot;tiktok&quot; |
| LINKEDIN | &quot;linkedin&quot; |
| PINTEREST | &quot;pinterest&quot; |
| GOOGLE | &quot;google&quot; |
| TWITTER | &quot;twitter&quot; |
| OPENAI | &quot;openai&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



