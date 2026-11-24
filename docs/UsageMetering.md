

# UsageMetering

Billed spend by product family over a window, from the usage-based invoice breakdown (the CHARGE view). Returned by `GET /v1/usage`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**supported** | **Boolean** | False for legacy Stripe accounts (no usage-based invoice to split); &#x60;days&#x60; and &#x60;totals&#x60; are then empty/zero. |  [optional] |
|**granularity** | [**GranularityEnum**](#GranularityEnum) |  |  [optional] |
|**days** | [**List&lt;UsageMeteringDaysInner&gt;**](UsageMeteringDaysInner.md) | One row per bucket. Empty when &#x60;granularity&#x3D;total&#x60;. &#x60;date&#x60; is a UTC date (month buckets use the 1st). |  [optional] |
|**totals** | [**UsageMeteringTotals**](UsageMeteringTotals.md) |  |  [optional] |
|**lineItems** | [**List&lt;UsageMeteringLineItemsInner&gt;**](UsageMeteringLineItemsInner.md) | Per-invoice-line-item rows (largest spend first) for a detailed breakdown. |  [optional] |
|**peaks** | [**UsageMeteringPeaks**](UsageMeteringPeaks.md) |  |  [optional] |
|**callUsage** | [**UsageMeteringCallUsage**](UsageMeteringCallUsage.md) |  |  [optional] |
|**period** | [**UsageMeteringPeriod**](UsageMeteringPeriod.md) |  |  [optional] |
|**tax** | [**UsageMeteringTax**](UsageMeteringTax.md) |  |  [optional] |
|**attribution** | [**UsageMeteringAttribution**](UsageMeteringAttribution.md) |  |  [optional] |
|**incomplete** | **Boolean** | Check it before rebilling. Present and true when a read behind the split failed: a group&#39;s spend can then be lower than the real one (it is &#x60;unattributed&#x60; in a full breakdown, missing from a view of some profiles or accounts). Retry in a minute. |  [optional] |
|**scope** | [**UsageMeteringScope**](UsageMeteringScope.md) |  |  [optional] |



## Enum: GranularityEnum

| Name | Value |
|---- | -----|
| DAY | &quot;day&quot; |
| MONTH | &quot;month&quot; |
| TOTAL | &quot;total&quot; |



