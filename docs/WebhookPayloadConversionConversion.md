

# WebhookPayloadConversionConversion


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventId** | **String** |  |  |
|**eventName** | **String** |  |  |
|**eventTime** | **OffsetDateTime** |  |  |
|**receivedAt** | **OffsetDateTime** |  |  |
|**source** | **String** | Who sent it: &#x60;api&#x60;, &#x60;relay&#x60;, a lead form (&#x60;meta_leads&#x60;, &#x60;google_leads&#x60;, &#x60;linkedin_leads&#x60;, &#x60;tiktok_leads&#x60;), a store (&#x60;shopify&#x60;, &#x60;woocommerce&#x60;), &#x60;stripe&#x60; or &#x60;hubspot&#x60;. |  |
|**actionSource** | **String** |  |  [optional] |
|**value** | **BigDecimal** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**sourceUrl** | **String** | Origin, path and attribution parameters only. |  [optional] |
|**utm** | [**StoredEventUtm**](StoredEventUtm.md) |  |  [optional] |
|**zrn** | **String** |  |  [optional] |
|**clickIds** | [**StoredEventClickIds**](StoredEventClickIds.md) |  |  [optional] |
|**destinationsSent** | **Integer** |  |  [optional] |
|**hasEmail** | **Boolean** |  |  [optional] |
|**hasPhone** | **Boolean** |  |  [optional] |
|**hasExternalId** | **Boolean** |  |  [optional] |
|**campaign** | [**WebhookPayloadConversionConversionCampaign**](WebhookPayloadConversionConversionCampaign.md) |  |  |
|**campaignMatch** | **String** | &#x60;matched&#x60;, or why there is no campaign: &#x60;no_hint&#x60;, &#x60;no_campaign&#x60;, &#x60;ambiguous&#x60;, &#x60;not_counted&#x60; or &#x60;match_failed&#x60;. |  |



