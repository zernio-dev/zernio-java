

# GetTopupInvoice200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **URI** |  |  |
|**format** | [**FormatEnum**](#FormatEnum) |  |  |
|**pdfUrl** | **URI** | The invoice PDF. |  |
|**pageUrl** | **URI** | The invoice&#39;s Stripe-hosted page. |  |
|**amountCents** | **Integer** | Amount added to your balance, as in the top-up list. |  |
|**taxCents** | **Integer** | Tax charged on top of amountCents. |  |
|**chargedCents** | **Integer** | What the card was charged, tax included. |  |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| PDF | &quot;pdf&quot; |
| PAGE | &quot;page&quot; |



