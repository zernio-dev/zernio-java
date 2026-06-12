

# InitiateWhatsAppCallRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**to** | **String** | Consumer wa_id (E.164 |  |
|**action** | [**ActionEnum**](#ActionEnum) | Omit to place a call. Set to send the consent prompt instead. |  [optional] |
|**bodyText** | **String** | Body text shown with the consent prompt (send_call_permission_request only). |  [optional] |
|**forwardTo** | **String** | Per-call destination override. Same accepted shape as the number&#39;s stored forwardTo (tel:+E164, sip:..., wss://...).  |  [optional] |
|**recordOverride** | **Boolean** |  |  [optional] |
|**bizOpaqueCallbackData** | **String** | Accepted for forward compatibility. Not currently echoed back in webhook payloads (SIP-first flow does not pass through Meta&#39;s Graph API where Meta would echo this).  |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| SEND_CALL_PERMISSION_REQUEST | &quot;send_call_permission_request&quot; |



