

# ConnectHandoff


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accounts** | [**List&lt;ConnectHandoffAccountsInner&gt;**](ConnectHandoffAccountsInner.md) | Filled when &#x60;status&#x60; is &#x60;connected&#x60;: every account the connect added (several when the user picked several pages, locations or organizations), each checked to be on the profile the connect was started for and written during this handoff. Empty otherwise. |  [optional] |
|**error** | [**ConnectHandoffError**](ConnectHandoffError.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| WAITING | &quot;waiting&quot; |
| OPENED | &quot;opened&quot; |
| CONNECTED | &quot;connected&quot; |
| FAILED | &quot;failed&quot; |
| EXPIRED | &quot;expired&quot; |



