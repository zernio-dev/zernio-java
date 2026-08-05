

# ValueRuleSet

A named set of bid-adjustment rules on an ad account. Attach it to an ad set with `valueRuleSetId`. Limits: 6 sets per ad account, 10 rules per set, 4 criteria per rule. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform value rule set id. |  |
|**name** | **String** |  |  |
|**rules** | [**List&lt;ValueRule&gt;**](ValueRule.md) | Evaluated in order; the first matching rule wins. |  |



