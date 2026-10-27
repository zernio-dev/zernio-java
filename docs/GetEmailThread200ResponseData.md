

# GetEmailThread200ResponseData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) |  |  [optional] |
|**subject** | **String** |  |  [optional] |
|**snippet** | **String** |  |  [optional] |
|**participants** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**messageIds** | **List&lt;String&gt;** |  |  [optional] |
|**draftIds** | **List&lt;String&gt;** |  |  [optional] |
|**folders** | **List&lt;String&gt;** |  |  [optional] |
|**hasAttachments** | **Boolean** |  |  [optional] |
|**hasDrafts** | **Boolean** |  |  [optional] |
|**unread** | **Boolean** |  |  [optional] |
|**starred** | **Boolean** |  |  [optional] |
|**earliestMessageAt** | **OffsetDateTime** |  |  [optional] |
|**latestMessageReceivedAt** | **OffsetDateTime** |  |  [optional] |
|**latestMessageSentAt** | **OffsetDateTime** |  |  [optional] |
|**messages** | [**List&lt;EmailMessage&gt;**](EmailMessage.md) |  |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |



