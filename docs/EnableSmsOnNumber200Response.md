

# EnableSmsOnNumber200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** |  |  [optional] |
|**id** | **String** | The SMS social account ID (present when enabled). |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**isActive** | **Boolean** | False for US numbers until their registration is approved. |  [optional] |
|**country** | **String** |  |  [optional] |
|**smsCapable** | **Boolean** | Null when capability can&#39;t be read yet (still provisioning). |  [optional] |
|**mmsCapable** | **Boolean** |  |  [optional] |
|**domesticOnly** | **Boolean** |  |  [optional] |
|**notReady** | **Boolean** | Number is still provisioning at the carrier; retry shortly. |  [optional] |
|**needsRegistration** | **Boolean** | US only; a carrier registration is required before delivery. |  [optional] |
|**alreadyRegistered** | **Boolean** | A prior non-rejected registration already covers this number; no re-submit needed. |  [optional] |
|**registrationStatus** | [**RegistrationStatusEnum**](#RegistrationStatusEnum) |  |  [optional] |
|**reusable** | [**EnableSmsOnNumber200ResponseReusable**](EnableSmsOnNumber200ResponseReusable.md) |  |  [optional] |
|**message** | **String** | Human-readable explanation when &#x60;enabled&#x60; is false. |  [optional] |



## Enum: RegistrationStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |



