

# WorkflowNode

A node in a workflow graph. `config` shape depends on `type`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable node id referenced by edges |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**config** | **Map&lt;String, Object&gt;** | Type-specific settings. trigger: { keywords:[string], matchType: any|contains|exact|regex, onlyFirstMessage:boolean }. send_message: { messageType: text|template|media|interactive, text, template:{name,language,variableMapping}, media:{mediaType,url,caption}, interactive } (template/interactive are WhatsApp-only). wait_for_reply: { timeoutMinutes:int, saveAs:string }. condition: { rules:[{ id, variable, operator: equals|not_equals|contains|not_contains|starts_with|ends_with|exists|not_exists|matches, value }] }. set_variable: { assignments:[{ name, value }] }. delay: { delayMinutes:int }. webhook: { url, method, headers, bodyTemplate, saveAs }. handoff: { note, assignTo }. String fields support {{variable}} interpolation.  |  [optional] |
|**position** | [**WorkflowNodePosition**](WorkflowNodePosition.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TRIGGER | &quot;trigger&quot; |
| SEND_MESSAGE | &quot;send_message&quot; |
| WAIT_FOR_REPLY | &quot;wait_for_reply&quot; |
| CONDITION | &quot;condition&quot; |
| SET_VARIABLE | &quot;set_variable&quot; |
| DELAY | &quot;delay&quot; |
| WEBHOOK | &quot;webhook&quot; |
| HANDOFF | &quot;handoff&quot; |
| END | &quot;end&quot; |



