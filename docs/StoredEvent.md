

# StoredEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventId** | **String** |  |  [optional] |
|**profileId** | **String** | The profile the event was stored under. |  [optional] |
|**source** | **String** | Where the event came from: &#x60;api&#x60;, &#x60;relay&#x60;, &#x60;web&#x60;, &#x60;shopify&#x60;, &#x60;woocommerce&#x60;, &#x60;stripe&#x60;, &#x60;hubspot&#x60;, &#x60;salesforce&#x60;, &#x60;gohighlevel&#x60;, &#x60;meta_leads&#x60;, &#x60;google_leads&#x60;, &#x60;linkedin_leads&#x60;, &#x60;tiktok_leads&#x60;, &#x60;form_leads&#x60; (a website form or &#x60;POST /v1/leads&#x60;) or &#x60;postback&#x60; (an affiliate network&#39;s postback to a tracking link). |  [optional] |
|**eventName** | **String** |  |  [optional] |
|**eventTime** | **OffsetDateTime** |  |  [optional] |
|**receivedAt** | **OffsetDateTime** |  |  [optional] |
|**actionSource** | **String** |  |  [optional] |
|**value** | **BigDecimal** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**sourceUrl** | **String** | Origin, path and attribution parameters only. |  [optional] |
|**utm** | [**StoredEventUtm**](StoredEventUtm.md) |  |  [optional] |
|**zrn** | **String** | Ad ID from the &#x60;zrn&#x60; parameter Zernio adds to links of ads it creates. |  [optional] |
|**clickIds** | [**StoredEventClickIds**](StoredEventClickIds.md) |  |  [optional] |
|**destinationsSent** | **Integer** | Destinations the event was forwarded to. |  [optional] |
|**hasEmail** | **Boolean** |  |  [optional] |
|**hasPhone** | **Boolean** |  |  [optional] |
|**hasExternalId** | **Boolean** |  |  [optional] |
|**pairedEventId** | **String** | In a &#x60;GET /v1/events&#x60; page: the other copy of the same conversion, when a website tag (&#x60;web&#x60;) and a server send both stored it under different event ids (same event name, a shared identifier, at most 30 minutes apart). &#x60;null&#x60; otherwise, and always &#x60;null&#x60; from &#x60;GET /v1/events/{eventId}&#x60;. |  [optional] |
|**ad** | [**StoredEventAd**](StoredEventAd.md) |  |  [optional] |
|**campaign** | [**StoredEventCampaign**](StoredEventCampaign.md) |  |  [optional] |
|**counted** | **Boolean** | &#x60;false&#x60; for a website (&#x60;web&#x60;) copy of an event name a server source also reported that day: the server copy counts in the overview and campaign results, and this one is kept but not counted. |  [optional] |



