

# AdRuleCondition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metric** | [**MetricEnum**](#MetricEnum) |  |  |
|**window** | [**WindowEnum**](#WindowEnum) |  |  |
|**op** | [**OpEnum**](#OpEnum) |  |  |
|**value** | **BigDecimal** |  |  |
|**compareTo** | **String** | Makes the condition relative: &#x60;value&#x60; becomes a ratio of the metric over &#x60;window&#x60; to the same metric over this window. &#x60;previous_period&#x60; is the same number of days just before &#x60;window&#x60;; any other value is a window, such as &#x60;30_to_2_days_ago&#x60;.  Spend, impressions, clicks, conversions and reach are compared per day, so windows of different lengths compare fairly; rates such as &#x60;cpc&#x60; compare as they are. A comparison window with no value never matches.  |  [optional] |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| SPEND | &quot;spend&quot; |
| IMPRESSIONS | &quot;impressions&quot; |
| CLICKS | &quot;clicks&quot; |
| CONVERSIONS | &quot;conversions&quot; |
| CTR | &quot;ctr&quot; |
| CPC | &quot;cpc&quot; |
| CPM | &quot;cpm&quot; |
| CPA | &quot;cpa&quot; |
| ROAS | &quot;roas&quot; |
| REACH | &quot;reach&quot; |
| FREQUENCY | &quot;frequency&quot; |
| DAILY_BUDGET | &quot;daily_budget&quot; |
| BUDGET_USED | &quot;budget_used&quot; |



## Enum: WindowEnum

| Name | Value |
|---- | -----|
| TODAY | &quot;today&quot; |
| YESTERDAY | &quot;yesterday&quot; |
| LAST_3D | &quot;last_3d&quot; |
| LAST_7D | &quot;last_7d&quot; |
| LAST_14D | &quot;last_14d&quot; |
| LAST_30D | &quot;last_30d&quot; |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| GREATER_THAN | &quot;&gt;&quot; |
| GREATER_THAN_OR_EQUAL_TO | &quot;&gt;&#x3D;&quot; |
| LESS_THAN | &quot;&lt;&quot; |
| LESS_THAN_OR_EQUAL_TO | &quot;&lt;&#x3D;&quot; |



