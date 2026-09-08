

# UpdateWhatsAppTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | WhatsApp social account ID |  |
|**language** | **String** | Language code of the variant to edit (e.g. en_US, es, pt_BR). Required when the family has several languages. Body only: a language query parameter on PATCH is a 400. |  [optional] |
|**components** | [**List&lt;WhatsAppTemplateComponent&gt;**](WhatsAppTemplateComponent.md) | Updated template components. Optional when only message_send_ttl_seconds changes; at least one of the two is required. |  [optional] |
|**messageSendTtlSeconds** | **Integer** | Delivery validity window in seconds: a message not delivered within it is dropped. Range depends on category: AUTHENTICATION 30 to 900, UTILITY 30 to 43200 (12h), MARKETING 43200 to 2592000 (30 days); -1 restores the 30-day default on AUTHENTICATION and UTILITY. Meta defaults to 600 for AUTHENTICATION and 30 days otherwise. If Meta later recategorises the template, it clears the TTL (read it back to check). |  [optional] |



