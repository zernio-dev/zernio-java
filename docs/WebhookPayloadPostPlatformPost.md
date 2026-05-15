

# WebhookPayloadPostPlatformPost


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**content** | **String** |  |  |
|**status** | **String** | Post-level status AT FIRE TIME. May still be &#x60;publishing&#x60; if other platforms haven&#39;t terminated; check this field rather than assuming.  |  |
|**scheduledFor** | **OffsetDateTime** |  |  |
|**publishedAt** | **OffsetDateTime** |  |  [optional] |
|**platforms** | [**List&lt;WebhookPayloadPostPostPlatformsInner&gt;**](WebhookPayloadPostPostPlatformsInner.md) |  |  |



