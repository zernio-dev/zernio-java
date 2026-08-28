

# CreateInboxConversationRequestHeaderLocation

WhatsApp only. Required to send a template whose approved header format is LOCATION: Meta only accepts the location's lat/long at send time, never at template creation, so there is nothing to fill in automatically. Cannot be combined with headerMedia (a template has exactly one header).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**latitude** | **BigDecimal** | Latitude in decimal degrees. |  |
|**longitude** | **BigDecimal** | Longitude in decimal degrees. |  |
|**name** | **String** | Location name shown to the recipient (e.g. a business name). |  [optional] |
|**address** | **String** | Location address shown to the recipient. |  [optional] |



