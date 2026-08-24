

# ConnectWhatsAppCredentials200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** |  |  [optional] |
|**registrationWarning** | **String** | Present when the account was created but Meta rejected the Cloud API registration. The number cannot send messages until this is resolved. |  [optional] |
|**webhookNotice** | **String** | Present when the WABA webhook subscription (with the Zernio override callback) succeeded. Explains the delivery cutover and warns against unsubscribing the app from the WABA afterward. |  [optional] |
|**account** | [**ConnectWhatsAppCredentials200ResponseAccount**](ConnectWhatsAppCredentials200ResponseAccount.md) |  |  [optional] |



