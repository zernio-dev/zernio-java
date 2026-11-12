

# CommerceOrderEditPreview

The order as the edit leaves it. Amounts are in the currency the buyer paid in.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**subtotal** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**total** | [**CommerceMoney**](CommerceMoney.md) |  |  [optional] |
|**outstanding** | [**CommerceMoney**](CommerceMoney.md) | What the buyer still owes. Negative when the edit leaves them overpaid: refund that with the refunds endpoint. |  [optional] |
|**lineItems** | [**List&lt;CommerceOrderEditPreviewLineItemsInner&gt;**](CommerceOrderEditPreviewLineItemsInner.md) |  |  [optional] |



