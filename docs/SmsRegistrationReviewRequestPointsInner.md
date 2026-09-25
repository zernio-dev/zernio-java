

# SmsRegistrationReviewRequestPointsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Point id to send back in &#x60;answers[].pointId&#x60;. |  |
|**title** | **String** |  |  |
|**detail** | **String** | What exactly is needed. |  |
|**answer** | [**AnswerEnum**](#AnswerEnum) |  |  |



## Enum: AnswerEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| LINK | &quot;link&quot; |
| FILE | &quot;file&quot; |
| LINK_OR_FILE | &quot;link_or_file&quot; |



