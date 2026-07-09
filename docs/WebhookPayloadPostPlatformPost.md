

# WebhookPayloadPostPlatformPost


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**content** | **String** |  |  |
|**status** | **String** | Post-level status AT FIRE TIME. May still be &#x60;publishing&#x60; if other platforms haven&#39;t terminated; check this field rather than assuming.  |  |
|**scheduledFor** | **OffsetDateTime** |  |  |
|**publishedAt** | **OffsetDateTime** |  |  [optional] |
|**platforms** | [**List&lt;WebhookPayloadPostPlatformPostPlatformsInner&gt;**](WebhookPayloadPostPlatformPostPlatformsInner.md) |  |  |
|**metadata** | **Map&lt;String, Object&gt;** | The free-form &#x60;metadata&#x60; object supplied when the post was created, echoed back so you can map events onto your own records. Omitted when the post was created without it. |  [optional] |



