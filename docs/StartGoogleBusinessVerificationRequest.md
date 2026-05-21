

# StartGoogleBusinessVerificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**method** | [**MethodEnum**](#MethodEnum) | The verification method. Selects which method-specific field below is required. |  |
|**languageCode** | **String** |  |  [optional] |
|**phoneNumber** | **String** | For PHONE_CALL / SMS. |  [optional] |
|**emailAddress** | **String** | For EMAIL. |  [optional] |
|**mailerContact** | **Object** | For ADDRESS (postcard) verification. |  [optional] |
|**context** | **Object** | ServiceBusinessContext (e.g. service address). Required for service-area businesses. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| ADDRESS | &quot;ADDRESS&quot; |
| EMAIL | &quot;EMAIL&quot; |
| PHONE_CALL | &quot;PHONE_CALL&quot; |
| SMS | &quot;SMS&quot; |
| AUTO | &quot;AUTO&quot; |
| VETTED_PARTNER | &quot;VETTED_PARTNER&quot; |



