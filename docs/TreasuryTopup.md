

# TreasuryTopup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) |  |  [optional] |
|**purpose** | [**PurposeEnum**](#PurposeEnum) | &#x60;balance&#x60; funds your balance; &#x60;payout_batch&#x60; is the card payment of one payout batch, which pays its creators directly. |  [optional] |
|**payoutBatch** | [**TreasuryTopupPayoutBatch**](TreasuryTopupPayoutBatch.md) |  |  [optional] |
|**feeCoveredByZernio** | **Boolean** | True for a &#x60;payout_batch&#x60; payment: Zernio pays the Stripe processing fee out of its transfer fee, so you are credited the whole charge. |  [optional] |
|**amountCents** | **Integer** | Gross amount charged |  [optional] |
|**stripeFeeCents** | **Integer** | Stripe processing fee you paid; null until Stripe reports it, 0 when Zernio covers it |  [optional] |
|**netCents** | **Integer** | Amount credited to your balance: gross minus the Stripe fee, or the whole charge when Zernio covers the fee; null until Stripe reports it |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;pending&#x60; until the card is charged (or 3D Secure is finished) and credited. &#x60;expired&#x60; means it ended unpaid: cancelled, or 3D Secure left unfinished for 30 minutes. Only &#x60;pending&#x60; counts toward pendingTopupCents. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**succeededAt** | **OffsetDateTime** |  |  [optional] |



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



