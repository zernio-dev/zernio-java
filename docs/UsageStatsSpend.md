

# UsageStatsSpend

Metronome users only. Current-period spend summary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentPeriodCents** | **Integer** | Total current-period spend in cents (all products combined). |  [optional] |
|**creditsRemainingCents** | **Integer** | Free-tier credit remaining in cents. Applied before any charge. |  [optional] |
|**xSpendCents** | **Integer** | Current-period X/Twitter API spend in cents, summed from &#x60;xApiCallsByOperation&#x60; × per-operation prices. Tier-agnostic (covers every price including the $0.200 URL tier). Rounded up for conservative enforcement against &#x60;xSpendLimitCents&#x60;.  |  [optional] |
|**xSpendLimitCents** | **Integer** | Monthly X spend cap set by the account owner, or null if no cap. When current X spend hits this cap, analytics and inbox sync are auto-paused for X accounts. Publishing is never blocked by this cap.  |  [optional] |



