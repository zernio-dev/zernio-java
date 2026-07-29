

# WebhookPayloadPostPlatformPlatform

The specific platform that just transitioned to a terminal state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Platform name (e.g. &#x60;twitter&#x60;, &#x60;tiktok&#x60;, &#x60;instagram&#x60;). |  |
|**status** | [**StatusEnum**](#StatusEnum) | Terminal status this event fires on. Matches the event suffix. |  |
|**platformPostId** | **String** | Platform-native post id. Present on &#x60;published&#x60; and &#x60;deleted&#x60;, absent on &#x60;failed&#x60;. |  [optional] |
|**publishedUrl** | **String** | Public URL to the platform-side post. Present on &#x60;published&#x60; (when the platform exposes one and it is not a draft) and on &#x60;deleted&#x60; (when one was recorded at publish time). |  [optional] |
|**error** | **String** | Error message from the platform. Present on &#x60;failed&#x60; only. |  [optional] |
|**deletedAt** | **OffsetDateTime** | When the platform-side deletion was detected by Zernio sync (ISO 8601). Present only on &#x60;post.platform.deleted&#x60;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PUBLISHED | &quot;published&quot; |
| FAILED | &quot;failed&quot; |
| DELETED | &quot;deleted&quot; |



