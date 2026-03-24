

# WebhookPayloadMessageConversation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**platformConversationId** | **String** |  |  [optional] |
|**participantId** | **String** |  |  [optional] |
|**participantName** | **String** |  |  [optional] |
|**participantUsername** | **String** |  |  [optional] |
|**participantPicture** | **String** |  |  [optional] |
|**participantVerifiedType** | [**ParticipantVerifiedTypeEnum**](#ParticipantVerifiedTypeEnum) | X/Twitter verified badge type. Only present for Twitter/X conversations. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: ParticipantVerifiedTypeEnum

| Name | Value |
|---- | -----|
| BLUE | &quot;blue&quot; |
| GOVERNMENT | &quot;government&quot; |
| BUSINESS | &quot;business&quot; |
| NONE | &quot;none&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



