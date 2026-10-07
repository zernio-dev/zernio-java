

# DialVoiceWebCallRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**to** | **String** | The number to call, E.164 with leading +. |  |
|**credentialId** | **String** | The WebRTC credential id returned by POST /v1/voice/calls/web (the registered browser). |  |
|**fromNumber** | **String** | Which of your voice-enabled numbers to call from (optional when you have one). |  [optional] |
|**recordOverride** | **Boolean** |  |  [optional] |
|**ringTimeoutSeconds** | **Integer** | Seconds to let the callee&#39;s phone ring before the call ends as no_answer. The destination carrier can end it sooner. |  [optional] |



