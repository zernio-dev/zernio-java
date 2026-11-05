

# CreateTopup201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**topupId** | **String** |  |  |
|**amountCents** | **Integer** | Credited to your balance once paid. |  |
|**taxCents** | **Integer** | Tax added on top of amountCents (VAT where it applies). 0 when reverse charged or outside the EU. |  |
|**totalCents** | **Integer** | What the card is charged: amountCents + taxCents. |  |
|**taxLabel** | **String** | The tax and its rate, for example \&quot;VAT 21%\&quot;. Null when no tax is charged. |  |
|**reverseCharge** | **Boolean** | True for an EU business with a valid VAT id: no VAT is charged and the invoice says reverse charge. |  |
|**feeCents** | **Integer** | Always 0: there is no card fee. Kept for older clients. |  |
|**chargedCents** | **Integer** | Same as totalCents. Kept for older clients. |  |
|**feeIsExact** | **Boolean** | Always true. Kept for older clients. |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**clientSecret** | **String** | PaymentIntent client secret for Stripe.js handleNextAction; set only when status is requires_action |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;succeeded&quot; |
| PROCESSING | &quot;processing&quot; |
| REQUIRES_ACTION | &quot;requires_action&quot; |



