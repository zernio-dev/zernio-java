

# CreateInboxConversationRequestTemplateCardsInnerButtonsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**index** | **Integer** | Zero-based position of the button within the card&#39;s buttons. |  |
|**subType** | [**SubTypeEnum**](#SubTypeEnum) | The button kind, which decides how the value is sent. |  |
|**value** | **String** | The value to send (quick_reply payload, or the URL dynamic suffix). |  |



## Enum: SubTypeEnum

| Name | Value |
|---- | -----|
| QUICK_REPLY | &quot;quick_reply&quot; |
| URL | &quot;url&quot; |



