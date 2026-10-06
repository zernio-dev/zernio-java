

# SetConversationThreadControlRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Social account ID |  |
|**action** | [**ActionEnum**](#ActionEnum) | &#x60;request&#x60; is Facebook and Instagram only. |  |
|**target** | [**TargetEnum**](#TargetEnum) | WhatsApp only. With action pass: send control to Meta Business Agent instead of the escalation partner. |  [optional] |
|**targetAppId** | **String** | Facebook and Instagram only, required with action pass: the Meta app id receiving the thread. |  [optional] |
|**metadata** | **String** | Free-form note forwarded verbatim to the app receiving control (its messaging_handovers webhook). |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| RELEASE | &quot;release&quot; |
| TAKE | &quot;take&quot; |
| PASS | &quot;pass&quot; |
| REQUEST | &quot;request&quot; |



## Enum: TargetEnum

| Name | Value |
|---- | -----|
| AI_AGENT | &quot;ai_agent&quot; |



