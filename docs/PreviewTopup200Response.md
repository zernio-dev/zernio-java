

# PreviewTopup200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountCents** | **Integer** | Credited to your balance. |  |
|**taxCents** | **Integer** | Tax added on top (VAT where it applies). |  |
|**totalCents** | **Integer** | What the card would be charged: amountCents + taxCents. |  |
|**taxLabel** | **String** | The tax and its rate, for example \&quot;VAT 21%\&quot;. Null when no tax is charged. |  |
|**reverseCharge** | **Boolean** | True for an EU business with a valid VAT id: no VAT, reverse charge. |  |



