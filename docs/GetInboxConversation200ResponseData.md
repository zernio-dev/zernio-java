

# GetInboxConversation200ResponseData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountUsername** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**participantName** | **String** |  |  [optional] |
|**participantId** | **String** |  |  [optional] |
|**participantVerifiedType** | [**ParticipantVerifiedTypeEnum**](#ParticipantVerifiedTypeEnum) | X verified badge type. Only present for X conversations. |  [optional] |
|**businessScopedUserId** | **String** | WhatsApp only. Meta business-scoped user ID (BSUID), the stable identity anchor; present when Meta has sent it for this participant. |  [optional] |
|**whatsappUsername** | **String** | WhatsApp only. The participant&#39;s WhatsApp username (e.g. &#x60;jane.shop&#x60;, no leading @). Not a stable identifier, because users can change it: useful for display, not recommended as an identity anchor. Captured from inbound messages, so older threads fill in on their next inbound. |  [optional] |
|**lastMessage** | **String** |  |  [optional] |
|**lastMessageAt** | **OffsetDateTime** |  |  [optional] |
|**updatedTime** | **OffsetDateTime** |  |  [optional] |
|**participants** | [**List&lt;UpdateFacebookPage200ResponseSelectedPage&gt;**](UpdateFacebookPage200ResponseSelectedPage.md) |  |  [optional] |
|**instagramProfile** | [**ListInboxConversations200ResponseDataInnerInstagramProfile**](ListInboxConversations200ResponseDataInnerInstagramProfile.md) |  |  [optional] |
|**metadata** | [**GetInboxConversation200ResponseDataMetadata**](GetInboxConversation200ResponseDataMetadata.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



## Enum: ParticipantVerifiedTypeEnum

| Name | Value |
|---- | -----|
| BLUE | &quot;blue&quot; |
| GOVERNMENT | &quot;government&quot; |
| BUSINESS | &quot;business&quot; |
| NONE | &quot;none&quot; |



