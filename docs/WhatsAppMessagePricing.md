

# WhatsAppMessagePricing

WhatsApp only. Meta's `pricing` object from the status webhook, camelCased. Present (possibly null) on every WhatsApp `message.sent`, `message.delivered`, `message.read` and `message.failed`; absent on other platforms. Meta includes it on `sent` and on one of `delivered` or `read`, so it is null on the others and usually on `failed`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billable** | **Boolean** | Whether Meta bills this message. Meta has announced it will deprecate this field. |  |
|**pricingModel** | **String** | &#x60;PMP&#x60; (per-message pricing) or &#x60;CBP&#x60; (conversation-based, messages before 2025-07-01). |  |
|**category** | **String** | Pricing category as Meta sends it, for example &#x60;marketing&#x60;, &#x60;marketing_lite&#x60;, &#x60;utility&#x60;, &#x60;authentication&#x60;, &#x60;authentication-international&#x60;, &#x60;service&#x60;, &#x60;referral_conversion&#x60;. |  |
|**type** | **String** | &#x60;regular&#x60; (billable), &#x60;free_customer_service&#x60; or &#x60;free_entry_point&#x60;. |  |



