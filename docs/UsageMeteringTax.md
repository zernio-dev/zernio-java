

# UsageMeteringTax

Estimated tax on the window's net `totals.total`, computed with Stripe Tax against the billing address (the same engine the real invoice uses; invoices apply exclusive tax, so the card is charged total + tax). Null when the account has no billing address on file, the total is zero or negative, or the estimate failed. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**taxUsd** | **BigDecimal** | Estimated tax in USD, added on top of &#x60;totals.total&#x60;. |  [optional] |
|**ratePercent** | **BigDecimal** | Combined rate percentage, e.g. 21. |  [optional] |
|**jurisdictionLabel** | **String** | Human jurisdiction label, e.g. \&quot;ES VAT\&quot; or \&quot;WA sales tax\&quot;. |  [optional] |
|**reverseCharge** | **Boolean** | True for EU/UK B2B reverse charge (0 tax added by design). |  [optional] |



