

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



