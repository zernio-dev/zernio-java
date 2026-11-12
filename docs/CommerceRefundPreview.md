

# CommerceRefundPreview

What a refund would return, computed by the platform. Amounts are in the currency the buyer paid in, which refunds are made in.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**maximumRefundable** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**subtotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**tax** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**shipping** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**lineItems** | [**List&lt;CommerceRefundPreviewLineItemsInner&gt;**](CommerceRefundPreviewLineItemsInner.md) |  |  [optional] |
|**transactions** | [**List&lt;CommerceRefundPreviewTransactionsInner&gt;**](CommerceRefundPreviewTransactionsInner.md) | The payments the money goes back to. |  [optional] |



