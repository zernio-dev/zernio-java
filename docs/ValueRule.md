

# ValueRule

One bid-adjustment rule. Rules are evaluated in ARRAY ORDER and only the first matching rule adjusts the bid for an overlapping audience, so the order is semantic. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform rule id. Echo it on &#x60;PUT&#x60; to KEEP this rule, omit it to CREATE a new one. A rule left out of the array entirely is DELETED.  |  [optional] |
|**name** | **String** |  |  |
|**adjustSign** | [**AdjustSignEnum**](#AdjustSignEnum) | Direction of the adjustment. There is no signed value field. |  |
|**adjustValue** | **Integer** | Unsigned percentage magnitude. &#x60;INCREASE&#x60; accepts 1-1000, &#x60;DECREASE&#x60; accepts 1-90. 0 is out of range on both.  |  |
|**status** | **String** | Meta returns &#x60;ACTIVE&#x60; here but documents no enum for the field. Treat it as a passthrough: echo whatever the &#x60;GET&#x60; returned, and do not synthesize values.  |  [optional] |
|**criteria** | [**List&lt;ValueRuleCriterion&gt;**](ValueRuleCriterion.md) | All criteria on a rule must match for the rule to fire. |  |



## Enum: AdjustSignEnum

| Name | Value |
|---- | -----|
| INCREASE | &quot;INCREASE&quot; |
| DECREASE | &quot;DECREASE&quot; |



