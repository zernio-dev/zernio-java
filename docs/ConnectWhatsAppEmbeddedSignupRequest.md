

# ConnectWhatsAppEmbeddedSignupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Authorization code from the WA_EMBEDDED_SIGNUP postMessage |  |
|**profileId** | **String** |  |  |
|**wabaId** | **String** | WhatsApp Business Account id, when the SDK reported one |  [optional] |
|**phoneNumberId** | **String** |  |  [optional] |
|**isCoexistence** | **Boolean** | Number is also live in the WhatsApp Business app |  [optional] |
|**expectedPhoneNumber** | **String** | Rejects the connect when Meta returns a different number |  [optional] |
|**redirectUrl** | **String** | Hosted signup page only. When present, the response also carries &#x60;redirectUrl&#x60;, the URL the user should land on, with the outcome mapped exactly like the redirect flow (success params, or &#x60;error&#x60; and &#x60;platform&#x60; with the same values). Must be an absolute http(s) URL or a custom app scheme. |  [optional] |
|**echoConnectToken** | **Boolean** | Hosted signup page only. Append the connect token to the success redirect, as the redirect flow does for API-key callers. |  [optional] |



