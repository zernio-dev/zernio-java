

# AutomationEventActionStepOneOf

Sends `text` in the person's conversation, from the account they reached. `{{event.<fact>}}` reads the event's facts.  On WhatsApp it sends only within 24 hours of the person's last message or call, and is skipped otherwise. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**text** | **String** |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MESSAGES_SEND | &quot;messages.send&quot; |



