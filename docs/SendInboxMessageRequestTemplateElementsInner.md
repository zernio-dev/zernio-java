

# SendInboxMessageRequestTemplateElementsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | Element title (max 80 chars). Required for Instagram/Facebook generic templates. |  [optional] |
|**subtitle** | **String** | Element subtitle (Instagram/Facebook only) |  [optional] |
|**imageUrl** | **String** | Element image URL (Instagram/Facebook only) |  [optional] |
|**buttons** | [**List&lt;SendInboxMessageRequestTemplateElementsInnerButtonsInner&gt;**](SendInboxMessageRequestTemplateElementsInnerButtonsInner.md) | Element buttons (Instagram/Facebook only) |  [optional] |
|**name** | **String** | WhatsApp only. Name of the approved template to send. |  [optional] |
|**language** | **String** | WhatsApp only. Template language code (e.g. en_US). |  [optional] |
|**components** | **List&lt;Map&lt;String, Object&gt;&gt;** | WhatsApp only. Meta Cloud API send-shape components array, forwarded to Meta verbatim. |  [optional] |



