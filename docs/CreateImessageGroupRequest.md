

# CreateImessageGroupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The iMessage account (sender) that opens the group |  |
|**contacts** | **List&lt;String&gt;** | Participant handles (E.164 phones or iMessage emails) |  |
|**text** | **String** | The first message |  |
|**name** | **String** | Group name (required for WhatsApp groups) |  [optional] |
|**channel** | [**ChannelEnum**](#ChannelEnum) |  |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| IMESSAGE | &quot;imessage&quot; |
| SMS | &quot;sms&quot; |
| RCS | &quot;rcs&quot; |
| WHATSAPP | &quot;whatsapp&quot; |



