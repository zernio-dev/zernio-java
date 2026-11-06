

# PreviewCampaignPayoutBatch200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**payoutCount** | **Integer** | Creators who would be paid. |  |
|**amountCents** | **Integer** | Total the creators receive. |  |
|**feeCents** | **Integer** | Zernio fee: 4% per creator, 50 cent minimum. |  |
|**taxCents** | **Integer** | VAT on the fee, 0 when none applies. |  |
|**totalCents** | **Integer** | What the card would be charged: amountCents + feeCents + taxCents. |  |
|**taxLabel** | **String** | For example \&quot;VAT 21%\&quot;. Null when there is no tax. |  |
|**reverseCharge** | **Boolean** | The fee is reverse charged: you account for the VAT. |  |



