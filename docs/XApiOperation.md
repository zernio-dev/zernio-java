

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
|**tier** | [**TierEnum**](#TierEnum) | Which aggregate price tier this operation falls into. |  [optional] |
|**triggeredBy** | [**List&lt;XApiOperationTriggeredByInner&gt;**](XApiOperationTriggeredByInner.md) | Zernio platform methods that emit this operation, with their metering rule. |  [optional] |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| X_API_005 | &quot;x_api_005&quot; |
| X_API_010 | &quot;x_api_010&quot; |
| X_API_015 | &quot;x_api_015&quot; |



