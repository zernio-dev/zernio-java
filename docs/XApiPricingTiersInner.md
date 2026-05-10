

# XApiPricingTiersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tier** | **String** | Tier key derived from price (e.g. &#x60;x_api_005&#x60; for $0.005, &#x60;x_api_200&#x60; for $0.200). The first three keys map to the legacy &#x60;xApiCalls&#x60; aggregate; new tiers (e.g. &#x60;x_api_200&#x60; for the URL tier added April 2026) are surfaced here but not in the legacy shape.  |  [optional] |
|**pricePerCallUsd** | **BigDecimal** |  |  [optional] |
|**operationCount** | **Integer** |  |  [optional] |



