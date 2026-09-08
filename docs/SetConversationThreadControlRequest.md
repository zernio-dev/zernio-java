

# SetConversationThreadControlRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Social account ID |  |
|**action** | [**ActionEnum**](#ActionEnum) |  |  |
|**target** | [**TargetEnum**](#TargetEnum) | With action pass: send control to Meta Business Agent instead of the escalation partner. |  [optional] |
|**metadata** | **String** | Free-form note forwarded verbatim to the app receiving control (its messaging_handovers webhook). |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| RELEASE | &quot;release&quot; |
| TAKE | &quot;take&quot; |
| PASS | &quot;pass&quot; |



## Enum: TargetEnum

| Name | Value |
|---- | -----|
| AI_AGENT | &quot;ai_agent&quot; |



