

# TreasuryTopup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) |  |  [optional] |
|**purpose** | [**PurposeEnum**](#PurposeEnum) | &#x60;balance&#x60; funds your balance; &#x60;payout_batch&#x60; is the card payment of one payout batch, which pays its creators directly. |  [optional] |
|**payoutBatch** | [**TreasuryTopupPayoutBatch**](TreasuryTopupPayoutBatch.md) |  |  [optional] |
|**feeCoveredByZernio** | **Boolean** | True for a balance top-up (there is no card fee) and a &#x60;payout_batch&#x60; payment: Zernio pays the Stripe processing fee, so you are credited the whole charge. False on a top-up made before 2026-11-05. |  [optional] |
|**amountCents** | **Integer** | The amount you asked for. A top-up charges exactly this and credits it whole. Top-ups from 2026-11-02 to 2026-11-05 charged a card fee on top and credited what Stripe delivered; older ones charged this amount and credited it minus the fee. |  [optional] |
|**feeCents** | **Integer** | Card fee you paid: 0 when Zernio covers it (feeCoveredByZernio). On an older top-up, the fee Stripe took once paid, the fee charged on top before, or null. |  [optional] |
|**chargedCents** | **Integer** | What your card was charged: amountCents, or amountCents plus the card fee on a top-up from 2026-11-02 to 2026-11-05. |  [optional] |
|**stripeFeeCents** | **Integer** | feeCents once the top-up is paid; null before. Kept for older clients: read feeCents. |  [optional] |
|**netCents** | **Integer** | Amount credited to your balance; null until paid. amountCents when feeCoveredByZernio; on an older top-up, what Stripe delivered. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;pending&#x60; until the card is charged (or 3D Secure is finished) and credited. &#x60;expired&#x60; means it ended unpaid: cancelled, or 3D Secure left unfinished for 30 minutes. Only &#x60;pending&#x60; counts toward pendingTopupCents. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**succeededAt** | **OffsetDateTime** |  |  [optional] |
|**hasInvoice** | **Boolean** | A Checkout invoice exists for this payment (Checkout payments before 2026-10-29). Every paid payment has a card receipt (getTopupReceipt); a paid top-up has a statement (getTopupStatement). |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| CARD | &quot;card&quot; |
| BANK_TRANSFER | &quot;bank_transfer&quot; |



## Enum: PurposeEnum

| Name | Value |
|---- | -----|
| BALANCE | &quot;balance&quot; |
| PAYOUT_BATCH | &quot;payout_batch&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |
| EXPIRED | &quot;expired&quot; |



