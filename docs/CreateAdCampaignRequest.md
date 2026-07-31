

# CreateAdCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. |  |
|**adAccountId** | **String** | Meta ad account id (act_&lt;n&gt;). |  |
|**name** | **String** |  |  |
|**goal** | [**GoalEnum**](#GoalEnum) | Mapped to the ODAX objective (same mapping as POST /v1/ads/create). |  |
|**specialAdCategories** | [**List&lt;SpecialAdCategoriesEnum&gt;**](#List&lt;SpecialAdCategoriesEnum&gt;) |  |  [optional] |
|**budgetAmount** | **BigDecimal** | Campaign-level (CBO) budget in whole currency units. Requires budgetType. |  [optional] |
|**budgetType** | [**BudgetTypeEnum**](#BudgetTypeEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**bidStrategy** | [**BidStrategyEnum**](#BidStrategyEnum) | Campaign bid strategy. Meta puts &#x60;bid_strategy&#x60; where the budget lives, so this applies only alongside a campaign budget (CBO). Previously settable only via &#x60;PUT /v1/ads/campaigns/{campaignId}&#x60;. |  [optional] |
|**bidAmount** | **BigDecimal** | Whole currency units (USD: 5 &#x3D; $5.00). Required for LOWEST_COST_WITH_BID_CAP and COST_CAP; ignored otherwise. |  [optional] |
|**roasAverageFloor** | **BigDecimal** | Decimal ROAS multiplier (2.0 &#x3D; 2.0x). Required for LOWEST_COST_WITH_MIN_ROAS. |  [optional] |



## Enum: GoalEnum

| Name | Value |
|---- | -----|
| ENGAGEMENT | &quot;engagement&quot; |
| TRAFFIC | &quot;traffic&quot; |
| AWARENESS | &quot;awareness&quot; |
| VIDEO_VIEWS | &quot;video_views&quot; |
| LEAD_GENERATION | &quot;lead_generation&quot; |
| LEAD_CONVERSION | &quot;lead_conversion&quot; |
| JOB_APPLICANTS | &quot;job_applicants&quot; |
| CONVERSIONS | &quot;conversions&quot; |
| APP_PROMOTION | &quot;app_promotion&quot; |
| CATALOG_SALES | &quot;catalog_sales&quot; |



## Enum: List&lt;SpecialAdCategoriesEnum&gt;

| Name | Value |
|---- | -----|
| HOUSING | &quot;HOUSING&quot; |
| EMPLOYMENT | &quot;EMPLOYMENT&quot; |
| CREDIT | &quot;CREDIT&quot; |
| ISSUES_ELECTIONS_POLITICS | &quot;ISSUES_ELECTIONS_POLITICS&quot; |
| FINANCIAL_PRODUCTS_SERVICES | &quot;FINANCIAL_PRODUCTS_SERVICES&quot; |
| ONLINE_GAMBLING_AND_GAMING | &quot;ONLINE_GAMBLING_AND_GAMING&quot; |



## Enum: BudgetTypeEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| LIFETIME | &quot;lifetime&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PAUSED | &quot;PAUSED&quot; |



## Enum: BidStrategyEnum

| Name | Value |
|---- | -----|
| LOWEST_COST_WITHOUT_CAP | &quot;LOWEST_COST_WITHOUT_CAP&quot; |
| LOWEST_COST_WITH_BID_CAP | &quot;LOWEST_COST_WITH_BID_CAP&quot; |
| COST_CAP | &quot;COST_CAP&quot; |
| LOWEST_COST_WITH_MIN_ROAS | &quot;LOWEST_COST_WITH_MIN_ROAS&quot; |



