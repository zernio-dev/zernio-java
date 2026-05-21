

# WebhookPayloadReactionReaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emoji** | **String** | The emoji reacted with. May be an empty string when &#x60;action&#x60; is &#x60;removed&#x60; on WhatsApp (Meta does not report which emoji was removed).  |  |
|**action** | [**ActionEnum**](#ActionEnum) |  |  |
|**messageId** | **String** | Internal Zernio message ID of the reacted-to message, when resolvable from the platform ID. |  [optional] |
|**platformMessageId** | **String** | Platform-native ID of the reacted-to message (e.g. WhatsApp wamid). |  |
|**sender** | [**WebhookPayloadReactionReactionSender**](WebhookPayloadReactionReactionSender.md) |  |  |
|**reactedAt** | **OffsetDateTime** |  |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ADDED | &quot;added&quot; |
| REMOVED | &quot;removed&quot; |



