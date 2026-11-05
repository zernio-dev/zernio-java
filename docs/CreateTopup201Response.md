

# CreateTopup201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**topupId** | **String** |  |  |
|**amountCents** | **Integer** | Charged and credited to your balance once paid. |  |
|**feeCents** | **Integer** | Always 0: there is no card fee. Kept for older clients. |  |
|**chargedCents** | **Integer** | What the card is charged: amountCents. Kept for older clients. |  |
|**feeIsExact** | **Boolean** | Always true. Kept for older clients. |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**clientSecret** | **String** | PaymentIntent client secret for Stripe.js handleNextAction; set only when status is requires_action |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;succeeded&quot; |
| PROCESSING | &quot;processing&quot; |
| REQUIRES_ACTION | &quot;requires_action&quot; |



