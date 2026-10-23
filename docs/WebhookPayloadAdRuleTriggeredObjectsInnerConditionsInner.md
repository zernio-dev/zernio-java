

# WebhookPayloadAdRuleTriggeredObjectsInnerConditionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metric** | **String** | &#x60;spend&#x60;, &#x60;impressions&#x60;, &#x60;clicks&#x60;, &#x60;conversions&#x60;, &#x60;ctr&#x60;, &#x60;cpc&#x60;, &#x60;cpm&#x60;, &#x60;cpa&#x60; or &#x60;roas&#x60;. New values may be added. |  |
|**window** | **String** | &#x60;today&#x60;, &#x60;yesterday&#x60;, &#x60;last_3d&#x60;, &#x60;last_7d&#x60;, &#x60;last_14d&#x60; or &#x60;last_30d&#x60;, in the account&#39;s calendar (see &#x60;run.today&#x60;). New values may be added. |  |
|**op** | [**OpEnum**](#OpEnum) |  |  |
|**value** | **BigDecimal** | The threshold set on the rule. |  |
|**actual** | **BigDecimal** | The object&#39;s value for the metric over the window. Null when it cannot be computed, for example a cost per action with no actions. |  |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| GREATER_THAN | &quot;&gt;&quot; |
| GREATER_THAN_OR_EQUAL_TO | &quot;&gt;&#x3D;&quot; |
| LESS_THAN | &quot;&lt;&quot; |
| LESS_THAN_OR_EQUAL_TO | &quot;&lt;&#x3D;&quot; |



