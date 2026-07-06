

# CreateVoiceCall200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**callId** | **String** | Internal Call doc ID |  [optional] |
|**telnyxCallControlId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**from** | **String** |  |  [optional] |
|**to** | **String** |  |  [optional] |
|**forwardTo** | **String** |  |  [optional] |
|**greeting** | **String** |  |  [optional] |
|**recordingEnabled** | **Boolean** |  |  [optional] |
|**transcriptionEnabled** | **Boolean** |  |  [optional] |
|**transcriptionLanguage** | [**TranscriptionLanguageEnum**](#TranscriptionLanguageEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DIALING | &quot;dialing&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| OUTBOUND | &quot;outbound&quot; |



## Enum: TranscriptionLanguageEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| EN | &quot;en&quot; |
| ES | &quot;es&quot; |



