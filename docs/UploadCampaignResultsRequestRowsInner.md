

# UploadCampaignResultsRequestRowsInner

Exactly one of `campaignId`, `utmCampaign` or `campaignName`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **LocalDate** | The day, at most 400 days ago. |  |
|**campaignId** | **String** | The platform campaign id. |  [optional] |
|**utmCampaign** | **String** | The &#x60;utm_campaign&#x60; value on the campaign&#39;s ads. |  [optional] |
|**campaignName** | **String** | The campaign&#39;s name, matched case-insensitively. |  [optional] |
|**adAccountId** | **String** | Platform ad account id. Narrows matching to one ad account. |  [optional] |
|**values** | **Map&lt;String, BigDecimal&gt;** | Metric key (snake_case, up to 40 characters) to a non-negative number. 1 to 20 per row. |  |



