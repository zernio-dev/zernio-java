

# AdRuleCondition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metric** | [**MetricEnum**](#MetricEnum) |  |  |
|**window** | [**WindowEnum**](#WindowEnum) |  |  |
|**op** | [**OpEnum**](#OpEnum) | &#x60;top&#x60; and &#x60;bottom&#x60; rank the rule&#39;s objects by the metric over the window, highest first for &#x60;top&#x60;, and match the first &#x60;value&#x60; (a whole number from 1 to 100). Objects with no value are not ranked; the run history shows each one&#39;s position. |  |
|**value** | **BigDecimal** |  |  |
|**compareTo** | **String** | Makes the condition relative: &#x60;value&#x60; becomes a ratio of the metric over &#x60;window&#x60; to the same metric over this window, such as &#x60;30_to_2_days_ago&#x60;.  &#x60;previous_period&#x60; is the same number of days just before &#x60;window&#x60;. For &#x60;this_month&#x60; it is the same days of last month, and for &#x60;last_month&#x60; the month before.  Spend, impressions, clicks, conversions and reach are compared per day, so windows of different lengths compare fairly; rates such as &#x60;cpc&#x60; compare as they are. A comparison window with no value never matches.  |  [optional] |



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
| DAY_OF_MONTH | &quot;day_of_month&quot; |
| WORKING_DAY_OF_MONTH | &quot;working_day_of_month&quot; |



## Enum: WindowEnum

| Name | Value |
|---- | -----|
| TODAY | &quot;today&quot; |
| YESTERDAY | &quot;yesterday&quot; |
| LAST_3D | &quot;last_3d&quot; |
| LAST_7D | &quot;last_7d&quot; |
| LAST_14D | &quot;last_14d&quot; |
| LAST_30D | &quot;last_30d&quot; |
| THIS_MONTH | &quot;this_month&quot; |
| LAST_MONTH | &quot;last_month&quot; |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| GREATER_THAN | &quot;&gt;&quot; |
| GREATER_THAN_OR_EQUAL_TO | &quot;&gt;&#x3D;&quot; |
| LESS_THAN | &quot;&lt;&quot; |
| LESS_THAN_OR_EQUAL_TO | &quot;&lt;&#x3D;&quot; |
| TOP | &quot;top&quot; |
| BOTTOM | &quot;bottom&quot; |



