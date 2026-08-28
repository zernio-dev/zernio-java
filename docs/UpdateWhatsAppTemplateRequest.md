

# UpdateWhatsAppTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | WhatsApp social account ID |  |
|**language** | **String** | Language code of the variant to edit (e.g. en_US, es, pt_BR). Required when the family has several languages. Body only: a language query parameter on PATCH is a 400. |  [optional] |
|**components** | [**List&lt;WhatsAppTemplateComponent&gt;**](WhatsAppTemplateComponent.md) | Updated template components |  |



