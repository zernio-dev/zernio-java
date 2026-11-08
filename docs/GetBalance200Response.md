

# GetBalance200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableCents** | **Integer** | Your balance. It goes negative after a dispute or refund of a spent top-up, or when pay-per-use already in flight lands past zero. The next top-up covers it. New payout batches are refused while it is negative. |  [optional] |
|**balanceBilling** | **Boolean** | True when the account pays pay-per-use from this prepaid balance (new signups). Absent otherwise: that pay-per-use is on the monthly invoice. |  [optional] |
|**spendableCents** | **Integer** | Balance billing only (absent otherwise). What pay-per-use can still spend: availableCents plus promoCents, minus usage not yet posted. At 0 or below, new pay-per-use answers 402 &#x60;insufficient_balance&#x60;. |  [optional] |
|**promoCents** | **Integer** | Balance billing only (absent otherwise). Promotional and support credit Zernio added to your balance. Pay-per-use spends it before availableCents. It is never paid out to payees and is not part of availableCents. |  [optional] |
|**payoutLockedCents** | **Integer** | Always 0. The balance no longer pays creators, so none of it is locked from them. |  [optional] |
|**payoutLocks** | [**List&lt;GetBalance200ResponsePayoutLocksInner&gt;**](GetBalance200ResponsePayoutLocksInner.md) | Always empty. The balance no longer pays creators. |  [optional] |
|**pendingCents** | **Integer** | Card top-ups paid before 2026-10-29 that were held and are moving to availableCents (within the hour). Always 0 after that. |  [optional] |
|**pendingReleases** | [**List&lt;GetBalance200ResponsePendingReleasesInner&gt;**](GetBalance200ResponsePendingReleasesInner.md) | The held card top-ups behind pendingCents. |  [optional] |
|**pendingTopupCents** | **Integer** | Top-ups started but not paid yet. |  [optional] |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) |  |  [optional] |
|**recentTopups** | [**List&lt;TreasuryTopup&gt;**](TreasuryTopup.md) |  |  [optional] |
|**recentCreditRecharges** | [**List&lt;GetBalance200ResponseRecentCreditRechargesInner&gt;**](GetBalance200ResponseRecentCreditRechargesInner.md) | Balance billing only (absent otherwise). The 10 newest auto top-ups paid from the account credit you held when you moved to the balance, newest first. Nothing was charged to your card and there is no invoice. The amount was added to promoCents with the credit&#39;s own expiry. |  [optional] |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| USD | &quot;usd&quot; |



