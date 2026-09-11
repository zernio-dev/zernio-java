

# WebhookPayloadMessageMetadataLocation

WhatsApp only. The location pin the user shared, forwarded verbatim from Meta. The message `text` is only the emoji preview (`📍 <name>`); the coordinates live here. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**latitude** | **BigDecimal** | Latitude in decimal degrees. |  [optional] |
|**longitude** | **BigDecimal** | Longitude in decimal degrees. |  [optional] |
|**name** | **String** | Location name, when the user shared a named place. |  [optional] |
|**address** | **String** | Street address, when Meta sends one. |  [optional] |



