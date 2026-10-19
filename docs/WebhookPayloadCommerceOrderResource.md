

# WebhookPayloadCommerceOrderResource

Identifiers only, never buyer data: read the order with GET /v1/commerce/orders/{orderId}.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**id** | **String** | Platform-native order id. |  [optional] |
|**status** | **CommerceOrderStatus** |  |  [optional] |
|**platformStatus** | **String** | Raw platform status, e.g. UNFULFILLED on Shopify or processing on WooCommerce. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ORDER | &quot;order&quot; |



