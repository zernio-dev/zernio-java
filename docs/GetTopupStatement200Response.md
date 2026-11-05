

# GetTopupStatement200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **URI** |  |  |
|**format** | [**FormatEnum**](#FormatEnum) |  |  |
|**pdfUrl** | **URI** | The statement PDF. |  |
|**pageUrl** | **URI** | The statement&#39;s Stripe-hosted page. |  |
|**amountCents** | **Integer** | Amount added to your balance, as in the top-up list. |  |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| PDF | &quot;pdf&quot; |
| PAGE | &quot;page&quot; |



