

# ListEvents200ResponseEventsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventId** | **String** |  |  [optional] |
|**source** | **String** | Where the event came from: &#x60;api&#x60;, &#x60;relay&#x60;, &#x60;web&#x60;, &#x60;shopify&#x60;, &#x60;woocommerce&#x60;, &#x60;hubspot&#x60;, &#x60;meta_leads&#x60;, &#x60;google_leads&#x60;, &#x60;linkedin_leads&#x60; or &#x60;tiktok_leads&#x60;. |  [optional] |
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
|**ad** | [**StoredEventAd**](StoredEventAd.md) |  |  [optional] |
|**deliveries** | [**List&lt;ListEvents200ResponseEventsInnerAllOfDeliveriesInner&gt;**](ListEvents200ResponseEventsInnerAllOfDeliveriesInner.md) | Each destination the event was forwarded to, with its latest send status. The full detail is on GET /v1/events/{eventId}. |  [optional] |



