

# RequestPhoneNumberWhatsAppCode200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** |  |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) |  |  [optional] |
|**alreadyVerified** | **Boolean** | Meta already reports the number as verified. No code is sent and the number is activated. |  [optional] |
|**replaced** | **Boolean** | Meta refused the original number, which had never been live, so it was replaced on the same record. |  [optional] |
|**newPhoneNumber** | **String** | The replacement number, present when &#x60;replaced&#x60; is true. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| SMS | &quot;SMS&quot; |
| VOICE | &quot;VOICE&quot; |



