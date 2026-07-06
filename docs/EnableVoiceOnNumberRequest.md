

# EnableVoiceOnNumberRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**forwardTo** | **String** | tel:+E164, sip:..., or wss://... destination for inbound calls. Empty string clears the forward (outbound-only); omitted preserves the current one. |  [optional] |
|**recordingEnabled** | **Boolean** |  |  [optional] |
|**transcriptionEnabled** | **Boolean** |  |  [optional] |
|**transcriptionLanguage** | [**TranscriptionLanguageEnum**](#TranscriptionLanguageEnum) |  |  [optional] |
|**voicemailEnabled** | **Boolean** | Voicemail is taken when there&#39;s no live destination. Default on. |  [optional] |
|**voicemailGreeting** | **String** | Custom spoken greeting; empty string restores the default. |  [optional] |
|**businessHoursEnabled** | **Boolean** | Outside the windows, inbound skips the forward and goes to voicemail. Off &#x3D; 24/7. |  [optional] |
|**businessHoursTimezone** | **String** | IANA timezone the windows are evaluated in. |  [optional] |
|**businessHours** | [**List&lt;EnableVoiceOnNumberRequestBusinessHoursInner&gt;**](EnableVoiceOnNumberRequestBusinessHoursInner.md) |  |  [optional] |
|**blockedCallers** | **List&lt;String&gt;** | E.164 numbers rejected before answer. Replaces the whole list; bare 10-digit values are normalized as US numbers. |  [optional] |
|**forwardCallerId** | [**ForwardCallerIdEnum**](#ForwardCallerIdEnum) | Caller ID on the forwarded leg: your number (&#x60;business&#x60;) or the original caller&#39;s (&#x60;caller&#x60;). |  [optional] |
|**ivrEnabled** | **Boolean** | IVR menu (supersedes the plain forward within business hours). |  [optional] |
|**ivrPrompt** | **String** |  |  [optional] |
|**ivrOptions** | [**List&lt;EnableVoiceOnNumberRequestIvrOptionsInner&gt;**](EnableVoiceOnNumberRequestIvrOptionsInner.md) |  |  [optional] |



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



