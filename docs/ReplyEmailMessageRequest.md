

# ReplyEmailMessageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**to** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  |
|**cc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**bcc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**replyTo** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**fromName** | **String** |  |  [optional] |
|**subject** | **String** | Optional on replies; the provider keeps the thread subject. |  |
|**text** | **String** | Plain-text body. One of &#x60;text&#x60; or &#x60;html&#x60; is required. |  [optional] |
|**html** | **String** |  |  [optional] |
|**attachments** | [**List&lt;SendEmailRequestAttachmentsInner&gt;**](SendEmailRequestAttachmentsInner.md) | 25 MB in total; 3 MB per attachment on Microsoft. |  [optional] |
|**headers** | **Map&lt;String, String&gt;** | Custom &#x60;X-&#x60; headers only. &#x60;List-Unsubscribe&#x60; is dropped on Microsoft and reported in &#x60;metadata.droppedHeaders&#x60;. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |
|**scheduledFor** | **OffsetDateTime** | Reserved; currently rejected. |  [optional] |
|**holdAsDraft** | **Boolean** | Reserved; currently rejected. |  [optional] |
|**trackOpens** | **Boolean** | Not available; must be false. |  [optional] |
|**trackLinks** | **Boolean** | Not available; must be false. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) |  |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| REPLY | &quot;reply&quot; |
| REPLY_ALL | &quot;replyAll&quot; |



