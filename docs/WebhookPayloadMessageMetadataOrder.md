

# WebhookPayloadMessageMetadataOrder

WhatsApp only. Cart submitted by the user from a commerce message (catalog, product, or product-list message). Meta's `order` object forwarded verbatim. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogId** | **String** | Meta catalog the ordered products belong to. |  [optional] |
|**text** | **String** | Optional free-text note the user attached to the cart. |  [optional] |
|**productItems** | [**List&lt;WebhookPayloadMessageMetadataOrderProductItemsInner&gt;**](WebhookPayloadMessageMetadataOrderProductItemsInner.md) |  |  [optional] |



