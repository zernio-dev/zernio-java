

# ListInboxConversations200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Opaque conversation identifier. Pass it back verbatim to any /v1/inbox/conversations/{conversationId} route; do not assume a fixed format. |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountUsername** | **String** |  |  [optional] |
|**participantId** | **String** |  |  [optional] |
|**participantName** | **String** |  |  [optional] |
|**participantPicture** | **String** |  |  [optional] |
|**participantVerifiedType** | [**ParticipantVerifiedTypeEnum**](#ParticipantVerifiedTypeEnum) | X verified badge type. Only present for X conversations. |  [optional] |
|**lastMessage** | **String** |  |  [optional] |
|**updatedTime** | **OffsetDateTime** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**unreadCount** | **Integer** | Number of unread messages |  [optional] |
|**threadControl** | [**ThreadControlEnum**](#ThreadControlEnum) | WhatsApp only, present once Meta Business Agent has touched the thread. ai_agent: the agent answers and new inbound arrive flagged metadata.standby; app: you hold control; other: another partner app does. Change it with POST /v1/inbox/conversations/{conversationId}/thread-control. |  [optional] |
|**url** | **String** | Direct link to open the conversation on the platform (if available) |  [optional] |
|**instagramProfile** | [**ListInboxConversations200ResponseDataInnerInstagramProfile**](ListInboxConversations200ResponseDataInnerInstagramProfile.md) |  |  [optional] |
|**metadata** | [**ListInboxConversations200ResponseDataInnerMetadata**](ListInboxConversations200ResponseDataInnerMetadata.md) |  |  [optional] |



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



## Enum: ThreadControlEnum

| Name | Value |
|---- | -----|
| APP | &quot;app&quot; |
| AI_AGENT | &quot;ai_agent&quot; |
| OTHER | &quot;other&quot; |



