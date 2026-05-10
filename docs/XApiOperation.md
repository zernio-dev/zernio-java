

# XApiOperation

A single X API operation with its per-call price and the Zernio platform methods that trigger it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operation** | **String** | Internal operation key. Matches keys in &#x60;xApiCallsByOperation&#x60;. |  [optional] |
|**eventType** | **String** | Metronome &#x60;event_type&#x60; emitted when this operation runs. |  [optional] |
|**displayName** | **String** | Human-readable label shown on Metronome invoices. |  [optional] |
|**pricePerCallUsd** | **BigDecimal** |  |  [optional] |
|**pricePerCallCents** | **BigDecimal** | Per-call price in cents. Fractional values are intentional. |  [optional] |
|**tier** | **String** | Tier key derived from &#x60;pricePerCallUsd&#x60; (e.g. &#x60;x_api_005&#x60; for $0.005, &#x60;x_api_200&#x60; for $0.200). Useful for grouping operations by price in dashboards.  |  [optional] |
|**triggeredBy** | [**List&lt;XApiOperationTriggeredByInner&gt;**](XApiOperationTriggeredByInner.md) | Zernio platform methods that emit this operation, with their metering rule. |  [optional] |



