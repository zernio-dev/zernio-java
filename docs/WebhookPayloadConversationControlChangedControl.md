

# WebhookPayloadConversationControlChangedControl


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**owner** | [**OwnerEnum**](#OwnerEnum) | Who answers now. ai_agent: Meta Business Agent; app: you; other: another partner app on the number. |  |
|**previousOwner** | [**PreviousOwnerEnum**](#PreviousOwnerEnum) | Owner before this change, null when the thread had never been agent-handled. |  |
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



