

# ListInboxMentions200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Mention document ID |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountUsername** | **String** |  |  [optional] |
|**content** | **String** | Text of the post that mentioned you |  [optional] |
|**permalink** | **String** | URL to the source post on LinkedIn |  [optional] |
|**authorUrn** | **String** | LinkedIn URN of the person who mentioned you |  [optional] |
|**organizationalEntity** | **String** | URN of the organization that was mentioned |  [optional] |
|**publishedAt** | **OffsetDateTime** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| LINKEDIN | &quot;linkedin&quot; |



