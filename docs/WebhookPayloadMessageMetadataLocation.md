

# WebhookPayloadMessageMetadataLocation

WhatsApp and iMessage. The location pin the user shared. On WhatsApp it is forwarded verbatim from Meta and the message `text` is only the emoji preview (`📍 <name>`); the coordinates live here. On iMessage it is parsed from a Maps link in `text`, which stays as sent. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**latitude** | **BigDecimal** | Latitude in decimal degrees. |  [optional] |
|**longitude** | **BigDecimal** | Longitude in decimal degrees. |  [optional] |
|**name** | **String** | Location name, when the user shared a named place. |  [optional] |
|**address** | **String** | Street address, when Meta sends one. |  [optional] |



