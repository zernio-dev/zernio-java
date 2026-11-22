

# ForwardingRuleValueOverride

The value this destination gets. `original` sends the event's own value; `fixed` sends `amount` for every event; `percent` sends `amount` percent of the event's value (30 sends 30%, rounded to cents), and leaves an event without a value without one. The currency is kept.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) |  |  |
|**amount** | **BigDecimal** | Required for &#x60;fixed&#x60; and &#x60;percent&#x60; (at most 1000 for &#x60;percent&#x60;); null for &#x60;original&#x60;. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| ORIGINAL | &quot;original&quot; |
| FIXED | &quot;fixed&quot; |
| PERCENT | &quot;percent&quot; |



