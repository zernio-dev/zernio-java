

# PayoutBatchItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**participantId** | **String** |  |  |
|**creator** | [**PayoutBatchItemCreator**](PayoutBatchItemCreator.md) |  |  |
|**amountCents** | **Integer** | What the creator receives, in full. |  |
|**feeCents** | **Integer** | Zernio fee on top: 4%, 50 cents minimum per payout. |  |
|**totalCents** | **Integer** | amountCents plus feeCents. |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;skipped&#x60;: payout setup not finished, or the card payment never completed. &#x60;failed&#x60;: Stripe refused the transfer. &#x60;refunded&#x60;: failed or skipped after the card hold; its payout, fee and VAT on the fee went back to the card through a credit note. The amount is payable again in every case. |  |
|**failureReason** | **String** | Why the item was not paid, in plain words. |  |
|**transferId** | **String** | The treasury transfer that paid this item. |  |
|**refundedCents** | **Integer** | What went back to the card for a &#x60;refunded&#x60; item: payout, fee and VAT on the fee. Null otherwise. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| PAID | &quot;paid&quot; |
| FAILED | &quot;failed&quot; |
| SKIPPED | &quot;skipped&quot; |
| REFUNDED | &quot;refunded&quot; |



