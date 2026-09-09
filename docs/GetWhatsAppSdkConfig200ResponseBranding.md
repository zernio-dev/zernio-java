

# GetWhatsAppSdkConfig200ResponseBranding

Skin chosen when the hosted signup session was issued (`brandName`, `primaryColor`, `language` on `GET /v1/connect/whatsapp?signup=hosted`). Null for API-key callers and for sessions issued without one.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandName** | **String** |  |  [optional] |
|**primaryColor** | **String** | Hex colour, #RRGGBB |  [optional] |
|**language** | [**LanguageEnum**](#LanguageEnum) |  |  [optional] |



## Enum: LanguageEnum

| Name | Value |
|---- | -----|
| EN | &quot;en&quot; |
| ES | &quot;es&quot; |



