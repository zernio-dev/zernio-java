

# WebhookPayloadMessageSentMetadataLocation

WhatsApp only. The location pin this message carries, in the same shape the inbox send API accepts. Present on API sends that passed `location`, and on Coexistence echoes of a pin shared from the WhatsApp Business app. The message `text` is only the emoji preview (`📍 <name>`); the pin itself lives here. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**latitude** | **BigDecimal** | Latitude in decimal degrees. |  [optional] |
|**longitude** | **BigDecimal** | Longitude in decimal degrees. |  [optional] |
|**name** | **String** | Location name, when one was given. |  [optional] |
|**address** | **String** | Street address, when one was given. |  [optional] |



