

# ConnectWhatsAppEmbeddedSignupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Authorization code from the FB.login response (authResponse.code) |  |
|**profileId** | **String** |  |  |
|**wabaId** | **String** | waba_id from the WA_EMBEDDED_SIGNUP message event |  [optional] |
|**phoneNumberId** | **String** | phone_number_id from the WA_EMBEDDED_SIGNUP message event. With wabaId it skips the number picker. |  [optional] |
|**isCoexistence** | **Boolean** | Set when the popup ended with the FINISH_WHATSAPP_BUSINESS_APP_ONBOARDING event, so the number stays live in the WhatsApp Business app |  [optional] |
|**expectedPhoneNumber** | **String** | Rejects the connect when Meta returns a different number |  [optional] |



