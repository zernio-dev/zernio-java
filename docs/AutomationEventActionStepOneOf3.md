

# AutomationEventActionStepOneOf3

Calls an http or https URL. Without `body`, a POST sends the event's type, id and facts as JSON. Fits every event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**url** | **URI** |  |  |
|**method** | [**MethodEnum**](#MethodEnum) |  |  [optional] |
|**headers** | **Map&lt;String, String&gt;** |  |  [optional] |
|**body** | **String** | May read &#x60;{{event.&lt;fact&gt;}}&#x60;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| WEBHOOK_CALL | &quot;webhook.call&quot; |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PUT | &quot;PUT&quot; |
| PATCH | &quot;PATCH&quot; |
| DELETE | &quot;DELETE&quot; |



