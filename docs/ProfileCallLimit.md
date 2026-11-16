

# ProfileCallLimit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limit** | **BigDecimal** | The limit, or null when none is set at this level. |  |
|**used** | **BigDecimal** | Used in the current window, calls still in progress included. |  |
|**remaining** | **BigDecimal** | What is left before the limit; null when there is no limit. |  |
|**window** | [**WindowEnum**](#WindowEnum) | &#x60;concurrent&#x60; counts calls in progress now; the rolling windows end now. |  |



## Enum: WindowEnum

| Name | Value |
|---- | -----|
| CONCURRENT | &quot;concurrent&quot; |
| ROLLING_HOUR | &quot;rolling_hour&quot; |
| ROLLING_24H | &quot;rolling_24h&quot; |



