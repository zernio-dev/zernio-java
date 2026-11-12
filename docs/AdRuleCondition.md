

# AdRuleCondition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metric** | [**MetricEnum**](#MetricEnum) |  |  |
|**window** | [**WindowEnum**](#WindowEnum) | Days in the ad account&#39;s own timezone. &#x60;last_7d&#x60; is the 7 full days before today; only &#x60;today&#x60; and &#x60;this_month&#x60; read the day in progress.  &#x60;this_month&#x60; runs from the 1st through today; &#x60;last_month&#x60; is the whole previous calendar month.  &#x60;&lt;from&gt;_to_&lt;to&gt;_days_ago&#x60; is any range of full days, both ends included, such as &#x60;8_to_2_days_ago&#x60; to skip the 2 most recent days while their conversions still arrive. &#x60;from&#x60; is at least &#x60;to&#x60; and at most 90.  &#x60;last_complete_hour&#x60;, &#x60;last_3h&#x60; and &#x60;today_so_far&#x60; read campaign totals hour by hour, on campaign rules for Meta and Google, and end at the latest hour whose numbers have settled, not at now. They take &#x60;spend&#x60;, &#x60;impressions&#x60;, &#x60;clicks&#x60;, &#x60;ctr&#x60;, &#x60;cpc&#x60; and &#x60;cpm&#x60;, and no &#x60;top&#x60; or &#x60;bottom&#x60;.  |  |
|**op** | [**OpEnum**](#OpEnum) | &#x60;top&#x60; and &#x60;bottom&#x60; rank the rule&#39;s objects by the metric over the window, highest first for &#x60;top&#x60;, and match the first &#x60;value&#x60; (a whole number from 1 to 100). Objects with no value are not ranked; the run history shows each one&#39;s position. |  |
|**value** | **BigDecimal** |  |  |
|**compareTo** | **String** | Makes the condition relative: &#x60;value&#x60; becomes a ratio of the metric over &#x60;window&#x60; to the same metric over this window, such as &#x60;30_to_2_days_ago&#x60;.  &#x60;previous_period&#x60; is the same number of days just before &#x60;window&#x60;. For &#x60;this_month&#x60; it is the same days of last month, and for &#x60;last_month&#x60; the month before.  Spend, impressions, clicks, conversions and reach are compared per day, so windows of different lengths compare fairly; rates such as &#x60;cpc&#x60; compare as they are. A comparison window with no value never matches.  &#x60;usual&#x60; compares with the median of the same window on the 4 previous weeks. For an hourly window that is the same hours on the 4 previous same weekdays, and for a window of up to 7 full days (not &#x60;today&#x60;) the same days moved back 1 to 4 weeks.  &#x60;usual&#x60; needs at least 3 of those weeks with a value, and takes no reach, frequency, budget or calendar metric.  On an hourly window, &#x60;compareTo&#x60; is &#x60;usual&#x60;, or for &#x60;ctr&#x60;, &#x60;cpc&#x60; and &#x60;cpm&#x60; a window of full days ending by yesterday and starting at most 35 days ago, read from the same hourly totals.  For example, &#x60;cpc&#x60; over &#x60;last_complete_hour&#x60; &#x60;&gt;&#x3D;&#x60; 5 against &#x60;last_30d&#x60; means the last hour&#39;s clicks cost 5 times their 30-day price.  |  [optional] |
|**of** | [**OfEnum**](#OfEnum) | Reads the usual value of the metric over &#x60;window&#x60; (as &#x60;compareTo: usual&#x60; defines it) instead of its current value, such as campaigns that usually get at least 50 impressions in the last 3 hours. Not combined with &#x60;compareTo&#x60;. |  [optional] |



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
| SEARCH_IMPRESSION_SHARE | &quot;search_impression_share&quot; |
| SEARCH_BUDGET_LOST_IMPRESSION_SHARE | &quot;search_budget_lost_impression_share&quot; |
| SEARCH_RANK_LOST_IMPRESSION_SHARE | &quot;search_rank_lost_impression_share&quot; |



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
| LAST_COMPLETE_HOUR | &quot;last_complete_hour&quot; |
| LAST_3H | &quot;last_3h&quot; |
| TODAY_SO_FAR | &quot;today_so_far&quot; |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| GREATER_THAN | &quot;&gt;&quot; |
| GREATER_THAN_OR_EQUAL_TO | &quot;&gt;&#x3D;&quot; |
| LESS_THAN | &quot;&lt;&quot; |
| LESS_THAN_OR_EQUAL_TO | &quot;&lt;&#x3D;&quot; |
| TOP | &quot;top&quot; |
| BOTTOM | &quot;bottom&quot; |



## Enum: OfEnum

| Name | Value |
|---- | -----|
| USUAL | &quot;usual&quot; |



