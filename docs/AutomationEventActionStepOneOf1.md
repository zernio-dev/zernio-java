

# AutomationEventActionStepOneOf1

Starts a flow of the automation's profile whose trigger is \"API call\", for the person the event is about, on the flow's account. The event's facts are its `event` variables.  An order's customer is reached by phone, so its flow is a WhatsApp flow. A flow starts once per event. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**workflowId** | **String** |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| WORKFLOWS_START | &quot;workflows.start&quot; |



