

# EnableVoiceOnNumber200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**pstnForwardTo** | **String** |  |  [optional] |
|**recordingEnabled** | **Boolean** |  |  [optional] |
|**transcriptionEnabled** | **Boolean** |  |  [optional] |
|**transcriptionLanguage** | [**TranscriptionLanguageEnum**](#TranscriptionLanguageEnum) |  |  [optional] |
|**voicemailEnabled** | **Boolean** |  |  [optional] |
|**voicemailGreeting** | **String** |  |  [optional] |
|**businessHoursEnabled** | **Boolean** |  |  [optional] |
|**businessHoursTimezone** | **String** |  |  [optional] |
|**businessHours** | [**List&lt;EnableVoiceOnNumber200ResponseBusinessHoursInner&gt;**](EnableVoiceOnNumber200ResponseBusinessHoursInner.md) |  |  [optional] |
|**blockedCallers** | **List&lt;String&gt;** |  |  [optional] |
|**forwardCallerId** | [**ForwardCallerIdEnum**](#ForwardCallerIdEnum) |  |  [optional] |
|**ivrEnabled** | **Boolean** |  |  [optional] |
|**ivrPrompt** | **String** |  |  [optional] |
|**ivrOptions** | [**List&lt;EnableVoiceOnNumber200ResponseIvrOptionsInner&gt;**](EnableVoiceOnNumber200ResponseIvrOptionsInner.md) |  |  [optional] |



## Enum: TranscriptionLanguageEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| EN | &quot;en&quot; |
| ES | &quot;es&quot; |



## Enum: ForwardCallerIdEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| CALLER | &quot;caller&quot; |



