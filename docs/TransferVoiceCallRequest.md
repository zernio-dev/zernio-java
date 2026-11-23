

# TransferVoiceCallRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**to** | **String** | +E164 phone number (tel: prefix optional) or a sip: URI. wss:// is not a valid transfer target. |  |
|**callerId** | [**CallerIdEnum**](#CallerIdEnum) | Caller ID shown on the transfer leg. &#x60;business&#x60; is your own number. &#x60;caller&#x60; is the original caller&#39;s number, for inbound calls only. The carrier may refuse &#x60;caller&#x60; on some routes: you get a 422, then retry with &#x60;business&#x60;. |  [optional] |



## Enum: CallerIdEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| CALLER | &quot;caller&quot; |



