

# AppLovinAdsPlatformData

AppLovin options in platformSpecificData. Campaign fields apply to a new campaign; assets, languages and brandInfo to the creative set (the ad).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignType** | [**CampaignTypeEnum**](#CampaignTypeEnum) | Required for a new campaign. |  [optional] |
|**os** | [**OsEnum**](#OsEnum) | APP campaigns. Required. |  [optional] |
|**packageName** | **String** | APP campaigns. Required. |  [optional] |
|**itunesId** | **Integer** | iOS APP campaigns. Required. |  [optional] |
|**websiteUrl** | **URI** | WEB campaigns. Required unless linkUrl is sent. |  [optional] |
|**biddingStrategy** | [**BiddingStrategyEnum**](#BiddingStrategyEnum) | Defaults to CPI billing for a CPI goal, CPM billing otherwise. TARGET_GOAL_WITH_CPI_BILLING takes an APP campaign with a CPI goal only. Set at creation only. |  [optional] |
|**goalType** | [**GoalTypeEnum**](#GoalTypeEnum) | APP takes all, WEB takes CPE, CPP and CHK_ROAS. Defaults from goal: app_promotion is CPI, conversions CPP, lead_generation CPE. Set at creation only. |  [optional] |
|**goalValue** | **BigDecimal** | The goal for every country (a cost, or a ROAS ratio). APP limits: CPI below 200, CPE and CPP below 500, AD_ROAS at least 0.1, CHK_ROAS at least 0.01, BLD_ROAS at least 0.05. Send this or countryGoalValues. |  [optional] |
|**countryGoalValues** | **Map&lt;String, BigDecimal&gt;** | Per-country goal values for targeted countries. |  [optional] |
|**roasDayTarget** | [**RoasDayTargetEnum**](#RoasDayTargetEnum) | Required for ROAS goals (and WEB CPP). APP takes DAY7 or DAY28, WEB DAY0 or DAY7. |  [optional] |
|**eventTarget** | **String** | Required for a CPE goal. |  [optional] |
|**countryBudgets** | **Map&lt;String, BigDecimal&gt;** | Per-country daily budgets, instead of budgetAmount. AppLovin budgets are daily only. |  [optional] |
|**tracking** | [**AppLovinAdsPlatformDataTracking**](AppLovinAdsPlatformDataTracking.md) |  |  [optional] |
|**audienceStrategy** | [**AudienceStrategyEnum**](#AudienceStrategyEnum) | WEB campaigns. |  [optional] |
|**assets** | [**List&lt;AppLovinAdsPlatformDataAssetsInner&gt;**](AppLovinAdsPlatformDataAssetsInner.md) | The creative set media: URLs Zernio uploads to AppLovin, or ids of assets already there. Needs a HOSTED_HTML asset, or an IMG_INTER_P image plus a VID_LONG_P or VID_SHORT_P video. |  [optional] |
|**languages** | **List&lt;String&gt;** | Creative set languages as AppLovin names them. All languages by default. |  [optional] |
|**brandInfo** | [**AppLovinAdsPlatformDataBrandInfo**](AppLovinAdsPlatformDataBrandInfo.md) |  |  [optional] |



## Enum: CampaignTypeEnum

| Name | Value |
|---- | -----|
| APP | &quot;APP&quot; |
| WEB | &quot;WEB&quot; |



## Enum: OsEnum

| Name | Value |
|---- | -----|
| IOS | &quot;IOS&quot; |
| ANDROID | &quot;ANDROID&quot; |



## Enum: BiddingStrategyEnum

| Name | Value |
|---- | -----|
| TARGET_GOAL_WITH_CPI_BILLING | &quot;TARGET_GOAL_WITH_CPI_BILLING&quot; |
| AUTO_BIDDING_WITH_CPM_BILLING | &quot;AUTO_BIDDING_WITH_CPM_BILLING&quot; |



## Enum: GoalTypeEnum

| Name | Value |
|---- | -----|
| CPI | &quot;CPI&quot; |
| CPE | &quot;CPE&quot; |
| CPP | &quot;CPP&quot; |
| AD_ROAS | &quot;AD_ROAS&quot; |
| CHK_ROAS | &quot;CHK_ROAS&quot; |
| BLD_ROAS | &quot;BLD_ROAS&quot; |



## Enum: RoasDayTargetEnum

| Name | Value |
|---- | -----|
| DAY0 | &quot;DAY0&quot; |
| DAY7 | &quot;DAY7&quot; |
| DAY28 | &quot;DAY28&quot; |



## Enum: AudienceStrategyEnum

| Name | Value |
|---- | -----|
| UNIVERSAL | &quot;UNIVERSAL&quot; |
| PROSPECTING | &quot;PROSPECTING&quot; |
| DISCOVERY | &quot;DISCOVERY&quot; |



