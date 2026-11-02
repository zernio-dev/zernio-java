

# GetTopupReceipt200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **URI** |  |  |
|**format** | [**FormatEnum**](#FormatEnum) |  |  |
|**amountCents** | **Integer** | As in the top-up list. |  |
|**feeCents** | **Integer** | Card fee paid, as in the top-up list. |  |
|**chargedCents** | **Integer** | What the card was charged, the total on the receipt. |  |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| PDF | &quot;pdf&quot; |
| PAGE | &quot;page&quot; |



