

# CreateRfPredictionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id (posting or ads variant). |  |
|**adAccountId** | **String** | Meta ad account id (act_&lt;n&gt;). |  |
|**budgetAmount** | **BigDecimal** | Whole currency units. Exactly one of budgetAmount / reach. |  [optional] |
|**reach** | **Integer** | Target unique reach. Exactly one of budgetAmount / reach. |  [optional] |
|**startDate** | **OffsetDateTime** | Campaign window start (must be in the future). |  |
|**endDate** | **OffsetDateTime** |  |  |
|**frequencyCap** | **Integer** | Max impressions per person over the window. |  [optional] |
|**targeting** | **Object** | Canonical camelCase TargetingSpec (same shape as /v1/ads/create&#39;s &#x60;targeting&#x60;). Defaults to countries: [US]. |  [optional] |
|**placements** | **Object** | Meta placements object (same shape as /v1/ads/create&#39;s &#x60;placements&#x60;). |  [optional] |



