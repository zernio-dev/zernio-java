

# FlowAutomationDefinitionTrigger


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Read from the graph&#39;s trigger node; sent, it must agree with it. Absent while the graph has no trigger node. |  [optional] |
|**accountId** | **String** | The account it runs on. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INBOUND_MESSAGE | &quot;inbound_message&quot; |
| API_CALL | &quot;api_call&quot; |
| WHATSAPP_EVENT | &quot;whatsapp_event&quot; |
| REFERRAL | &quot;referral&quot; |
| STORY_MENTION | &quot;story_mention&quot; |
| COMMENT | &quot;comment&quot; |
| REACTION | &quot;reaction&quot; |
| LEAD_RECEIVED | &quot;lead_received&quot; |



