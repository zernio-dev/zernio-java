

# ForwardingRuleValueCondition

Forward only events whose value is greater than (`gt`), less than (`lt`) or equal to (`eq`) `amount`. An event without a value counts as 0. Checked on the value as received, before `valueOverride`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operator** | [**OperatorEnum**](#OperatorEnum) |  |  |
|**amount** | **BigDecimal** |  |  |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| GT | &quot;gt&quot; |
| LT | &quot;lt&quot; |
| EQ | &quot;eq&quot; |



