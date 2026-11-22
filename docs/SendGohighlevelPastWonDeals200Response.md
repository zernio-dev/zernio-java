

# SendGohighlevelPastWonDeals200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) |  |  |
|**sent** | **Integer** | Deals sent in this call. |  [optional] |
|**failed** | **Integer** | Deals that could not be sent in this call. |  [optional] |
|**remaining** | **Integer** | Unsent deals left for the next call. |  [optional] |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| SENT | &quot;sent&quot; |
| RELAY_OFF | &quot;relay_off&quot; |



