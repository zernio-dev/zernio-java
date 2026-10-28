

# PayoutBatchItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**participantId** | **String** |  |  |
|**creator** | [**PayoutBatchItemCreator**](PayoutBatchItemCreator.md) |  |  |
|**amountCents** | **Integer** | What the creator receives, in full. |  |
|**feeCents** | **Integer** | Zernio fee on top: 4% with a 50 cent minimum. |  |
|**totalCents** | **Integer** | amountCents plus feeCents. |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;skipped&#x60;: not paid because payout setup was not finished, or the card payment never completed; the amount is payable again. &#x60;failed&#x60;: Stripe refused the transfer; the amount is payable again. |  |
|**failureReason** | **String** | Why the item was not paid, in plain words. |  |
|**transferId** | **String** | The treasury transfer that paid this item. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| PAID | &quot;paid&quot; |
| FAILED | &quot;failed&quot; |
| SKIPPED | &quot;skipped&quot; |



