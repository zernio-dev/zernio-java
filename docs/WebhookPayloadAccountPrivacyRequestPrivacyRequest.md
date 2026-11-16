

# WebhookPayloadAccountPrivacyRequestPrivacyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | customer_data_request: the merchant asked for the data you hold about &#x60;customer&#x60;. Send it to the merchant.  customer_redact: erase the data you hold about &#x60;customer&#x60; and the orders in &#x60;orderIds&#x60;.  shop_redact: erase the data you hold about the whole shop. Sent 48 hours after the merchant uninstalled the app. |  |
|**shopDomain** | **String** |  |  |
|**shopId** | **String** |  |  |
|**customer** | [**WebhookPayloadAccountPrivacyRequestPrivacyRequestCustomer**](WebhookPayloadAccountPrivacyRequestPrivacyRequestCustomer.md) |  |  |
|**orderIds** | **List&lt;String&gt;** | The Shopify order ids the request covers. Empty for shop_redact. |  |
|**dataRequestId** | **String** | Shopify&#39;s id for a customer_data_request. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_DATA_REQUEST | &quot;customer_data_request&quot; |
| CUSTOMER_REDACT | &quot;customer_redact&quot; |
| SHOP_REDACT | &quot;shop_redact&quot; |



