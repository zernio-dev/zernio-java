

# UsageMetering

Billed spend by product family over a window, from Metronome's invoice breakdown (the CHARGE view). Returned by `GET /v1/usage`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**supported** | **Boolean** | False for legacy Stripe accounts (no Metronome invoice to split); &#x60;days&#x60; and &#x60;totals&#x60; are then empty/zero. |  [optional] |
|**granularity** | [**GranularityEnum**](#GranularityEnum) |  |  [optional] |
|**days** | [**List&lt;UsageMeteringDaysInner&gt;**](UsageMeteringDaysInner.md) | One row per bucket. Empty when &#x60;granularity&#x3D;total&#x60;. &#x60;date&#x60; is a UTC date (month buckets use the 1st). |  [optional] |
|**totals** | [**UsageMeteringTotals**](UsageMeteringTotals.md) |  |  [optional] |
|**lineItems** | [**List&lt;UsageMeteringLineItemsInner&gt;**](UsageMeteringLineItemsInner.md) | Per-invoice-line-item rows (largest spend first) for a detailed breakdown. |  [optional] |
|**peaks** | [**UsageMeteringPeaks**](UsageMeteringPeaks.md) |  |  [optional] |
|**callUsage** | [**UsageMeteringCallUsage**](UsageMeteringCallUsage.md) |  |  [optional] |
|**period** | [**UsageMeteringPeriod**](UsageMeteringPeriod.md) |  |  [optional] |
|**tax** | [**UsageMeteringTax**](UsageMeteringTax.md) |  |  [optional] |



## Enum: GranularityEnum

| Name | Value |
|---- | -----|
| DAY | &quot;day&quot; |
| MONTH | &quot;month&quot; |
| TOTAL | &quot;total&quot; |



