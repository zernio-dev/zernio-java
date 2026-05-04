

# XApiPricing

Canonical X/Twitter API pricing table. Zernio passes X API costs through at exact rates with zero markup, so every call you make has a known per-unit price. Use this payload alongside `/v1/usage-stats` (which returns per-operation call counts via `xApiCallsByOperation`) to compute exact cost attribution by X action. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currency** | **String** |  |  [optional] |
|**markup** | **String** | Always 0% — Zernio does not mark up X API rates. |  [optional] |
|**source** | **URI** |  |  [optional] |
|**lastVerified** | **LocalDate** | Date the prices were last verified against X&#39;s published rates. |  [optional] |
|**tiers** | [**List&lt;XApiPricingTiersInner&gt;**](XApiPricingTiersInner.md) | Rollup of operations grouped by their per-call price. |  [optional] |
|**operations** | [**List&lt;XApiOperation&gt;**](XApiOperation.md) | Flat list of every X operation Zernio can perform, with its rate. |  [optional] |



