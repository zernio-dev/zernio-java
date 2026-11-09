

# StoredEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventId** | **String** |  |  [optional] |
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



