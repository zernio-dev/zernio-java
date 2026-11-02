

# CreateTopup201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**topupId** | **String** |  |  |
|**amountCents** | **Integer** | Credited to your balance once paid: exactly this when feeIsExact, else at least this. |  |
|**feeCents** | **Integer** | Card fee, charged on top of amountCents. |  |
|**chargedCents** | **Integer** | What the card is charged: amountCents plus feeCents. |  |
|**feeIsExact** | **Boolean** | True when feeCents is exactly Stripe&#39;s fee for this card. False when it is the region&#39;s highest rate, so Stripe may take less and the difference is added to your balance. |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**clientSecret** | **String** | PaymentIntent client secret for Stripe.js handleNextAction; set only when status is requires_action |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;succeeded&quot; |
| PROCESSING | &quot;processing&quot; |
| REQUIRES_ACTION | &quot;requires_action&quot; |



