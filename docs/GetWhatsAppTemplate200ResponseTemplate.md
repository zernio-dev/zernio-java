

# GetWhatsAppTemplate200ResponseTemplate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Meta template id. Unique per language variant; usable on /v1/whatsapp/templates/id/{templateId}. |  [optional] |
|**name** | **String** |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**category** | **String** |  |  [optional] |
|**language** | **String** | The variant actually returned. |  [optional] |
|**components** | **List&lt;Object&gt;** |  |  [optional] |
|**rejectedReason** | **String** | Only when status is REJECTED. |  [optional] |
|**qualityScore** | **Object** | Post-approval quality (GREEN/YELLOW/RED), when Meta reports one. |  [optional] |



