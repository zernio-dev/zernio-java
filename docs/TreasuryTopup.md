

# TreasuryTopup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) |  |  [optional] |
|**purpose** | [**PurposeEnum**](#PurposeEnum) | &#x60;balance&#x60; funds your balance; &#x60;payout_batch&#x60; is the card payment of one payout batch, which pays its creators directly. |  [optional] |
|**payoutBatch** | [**TreasuryTopupPayoutBatch**](TreasuryTopupPayoutBatch.md) |  |  [optional] |
|**feeCoveredByZernio** | **Boolean** | True for a &#x60;payout_batch&#x60; payment: Zernio pays the Stripe processing fee out of its transfer fee, so you are credited the whole charge. |  [optional] |
|**amountCents** | **Integer** | The amount you asked for. A top-up charges the card fee on top of it and credits what Stripe delivers, at least this amount. Older top-ups charged this amount and credited it minus the fee. |  [optional] |
|**feeCents** | **Integer** | Card fee. Once paid, the fee Stripe took (chargedCents minus netCents). Before, the fee charged on top, or null on an older top-up. 0 when Zernio covers it (&#x60;payout_batch&#x60;). |  [optional] |
|**chargedCents** | **Integer** | What your card was charged: amountCents plus the card fee charged on top, or amountCents on an older top-up and on a &#x60;payout_batch&#x60; payment. |  [optional] |
|**stripeFeeCents** | **Integer** | feeCents once the top-up is paid; null before. Kept for older clients: read feeCents. |  [optional] |
|**netCents** | **Integer** | Amount credited to your balance, what Stripe delivered; null until paid. At least amountCents on a top-up that charged the fee on top, and amountCents on &#x60;payout_batch&#x60; payments. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;pending&#x60; until the card is charged (or 3D Secure is finished) and credited. &#x60;expired&#x60; means it ended unpaid: cancelled, or 3D Secure left unfinished for 30 minutes. Only &#x60;pending&#x60; counts toward pendingTopupCents. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**succeededAt** | **OffsetDateTime** |  |  [optional] |
|**hasInvoice** | **Boolean** | A Stripe invoice exists for this payment (Checkout payments). Every paid payment has a card receipt; see getTopupReceipt. |  [optional] |



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



