

# PostAuthenticityReasonsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) |  |  |
|**weight** | **BigDecimal** | Points taken off 100. Zero for no_watch_signal, which only lowers confidence. |  |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| LATE_BLOCK | &quot;late_block&quot; |
| FLAT_ENGAGEMENT | &quot;flat_engagement&quot; |
| VIEW_FOLLOWER_GAP | &quot;view_follower_gap&quot; |
| CAP_SEEKING | &quot;cap_seeking&quot; |
| PRIOR_FLAGS | &quot;prior_flags&quot; |
| NO_WATCH_SIGNAL | &quot;no_watch_signal&quot; |



