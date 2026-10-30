

# AdRuleCondition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metric** | [**MetricEnum**](#MetricEnum) |  |  |
|**window** | [**WindowEnum**](#WindowEnum) | Days in the ad account&#39;s own timezone. &#x60;last_7d&#x60; is the 7 full days before today; only &#x60;today&#x60; reads the day in progress. |  |
|**op** | [**OpEnum**](#OpEnum) |  |  |
|**value** | **BigDecimal** |  |  |



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



