

# WebhookPayloadConversationStartedConversation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Internal conversation ID |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**platformConversationId** | **String** |  |  |
|**participantId** | **String** | Contact&#39;s platform identifier (IGSID |  [optional] |
|**participantName** | **String** |  |  |
|**participantUsername** | **String** | Contact&#39;s handle when the platform exposes one |  [optional] |
|**participantPicture** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| TELEGRAM | &quot;telegram&quot; |
| WHATSAPP | &quot;whatsapp&quot; |
| TWITTER | &quot;twitter&quot; |
| REDDIT | &quot;reddit&quot; |
| BLUESKY | &quot;bluesky&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



