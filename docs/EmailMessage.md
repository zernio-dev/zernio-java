

# EmailMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The provider&#39;s message id. |  [optional] |
|**threadId** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) |  |  [optional] |
|**folders** | **List&lt;String&gt;** |  |  [optional] |
|**from** | [**EmailAddress**](EmailAddress.md) |  |  [optional] |
|**to** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**cc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**bcc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**replyTo** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**subject** | **String** |  |  [optional] |
|**snippet** | **String** |  |  [optional] |
|**text** | **String** |  |  [optional] |
|**html** | **String** |  |  [optional] |
|**attachments** | [**List&lt;EmailAttachment&gt;**](EmailAttachment.md) |  |  [optional] |
|**headers** | **Map&lt;String, String&gt;** | Only with &#x60;includeHeaders&#x3D;true&#x60;. |  [optional] |
|**raw** | **String** | MIME source, only with &#x60;raw&#x3D;true&#x60;. |  [optional] |
|**date** | **OffsetDateTime** |  |  [optional] |
|**unread** | **Boolean** |  |  [optional] |
|**starred** | **Boolean** |  |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |



