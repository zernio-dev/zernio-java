

# WebhookPayloadConversationControlChangedControl


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**owner** | [**OwnerEnum**](#OwnerEnum) | Who answers now. ai_agent: Meta Business Agent (WhatsApp); app: you; other: another app (a WhatsApp partner, or a Messenger / Instagram receiver such as Page Inbox). |  |
|**previousOwner** | [**PreviousOwnerEnum**](#PreviousOwnerEnum) | Owner before this change, null when no handover had touched the thread. |  |
|**ownerAppId** | **String** | Meta app id of the new owner, when Meta names it (Facebook and Instagram handovers, WhatsApp partner apps). Page Inbox is 263902037430900. |  [optional] |
|**metadata** | **String** | Free-form string the transferring app attached to the handover, forwarded verbatim. |  [optional] |



## Enum: OwnerEnum

| Name | Value |
|---- | -----|
| APP | &quot;app&quot; |
| AI_AGENT | &quot;ai_agent&quot; |
| OTHER | &quot;other&quot; |



## Enum: PreviousOwnerEnum

| Name | Value |
|---- | -----|
| APP | &quot;app&quot; |
| AI_AGENT | &quot;ai_agent&quot; |
| OTHER | &quot;other&quot; |



