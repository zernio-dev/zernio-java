

# CreateCommerceRefundRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Connected store SocialAccount id. |  |
|**lineItems** | [**List&lt;CommerceRefundRequestLineItemsInner&gt;**](CommerceRefundRequestLineItemsInner.md) |  |  [optional] |
|**shipping** | [**CommerceRefundRequestShipping**](CommerceRefundRequestShipping.md) |  |  [optional] |
|**amount** | **String** | Refund this much money instead of what the lines and shipping are worth, for a goodwill refund or a partial one. Taken from the order&#39;s payments in order, up to what each can still refund. |  [optional] |
|**currency** | **String** | The currency your amounts are in. Refused (400) unless it is the one the buyer paid in, which every refund amount uses. |  [optional] |
|**note** | **String** | Kept on the refund, visible to staff. |  [optional] |
|**notifyCustomer** | **Boolean** | Email the buyer about the refund. |  [optional] |
|**validateOnly** | **Boolean** | Return the refund the platform would make, without refunding anything. |  [optional] |



