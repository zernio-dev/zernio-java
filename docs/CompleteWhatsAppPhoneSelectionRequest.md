

# CompleteWhatsAppPhoneSelectionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | The Zernio profile ID |  |
|**phoneNumberId** | **String** | The selected phone number ID (from listWhatsAppPhoneNumbers) |  |
|**wabaId** | **String** | The WABA ID containing the selected phone |  |
|**tempToken** | **String** | The temporary access token from the headless redirect. Required unless sent in the X-Temp-Token header. |  [optional] |
|**connectFlow** | **String** | Set by the Zernio-hosted picker, whose user token stays in an httpOnly cookie. Integrators send tempToken instead. |  [optional] |
|**userProfile** | **Object** | Optional user profile data (passthrough) |  [optional] |
|**redirectUrl** | **String** | Optional URL to receive the post-connection redirect target |  [optional] |



