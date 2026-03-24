

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
|**participantVerifiedType** | [**ParticipantVerifiedTypeEnum**](#ParticipantVerifiedTypeEnum) | X/Twitter verified badge type. Only present for Twitter/X conversations. |  [optional] |
|**lastMessage** | **String** |  |  [optional] |
|**lastMessageAt** | **OffsetDateTime** |  |  [optional] |
|**updatedTime** | **OffsetDateTime** |  |  [optional] |
|**participants** | [**List&lt;UpdateFacebookPage200ResponseSelectedPage&gt;**](UpdateFacebookPage200ResponseSelectedPage.md) |  |  [optional] |
|**instagramProfile** | [**ListInboxConversations200ResponseDataInnerInstagramProfile**](ListInboxConversations200ResponseDataInnerInstagramProfile.md) |  |  [optional] |



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



