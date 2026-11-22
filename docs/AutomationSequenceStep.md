

# AutomationSequenceStep

Waits `after` the previous step (the first, after the enrollment), then sends `message`, or `template` on WhatsApp. Needs `message.text`, `message.attachments` or `template.name`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**after** | **String** | Whole minutes as a duration, such as &#x60;0m&#x60;, &#x60;90m&#x60; or &#x60;1d&#x60;. |  |
|**message** | [**AutomationSequenceStepMessage**](AutomationSequenceStepMessage.md) |  |  [optional] |
|**template** | [**AutomationSequenceStepTemplate**](AutomationSequenceStepTemplate.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MESSAGES_SEND | &quot;messages.send&quot; |



