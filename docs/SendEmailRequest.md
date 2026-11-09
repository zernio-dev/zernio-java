

# SendEmailRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**to** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  |
|**cc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**bcc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**replyTo** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**fromName** | **String** |  |  [optional] |
|**subject** | **String** |  |  |
|**text** | **String** | Plain-text body. One of &#x60;text&#x60; or &#x60;html&#x60; is required. |  [optional] |
|**html** | **String** |  |  [optional] |
|**attachments** | [**List&lt;SendEmailRequestAttachmentsInner&gt;**](SendEmailRequestAttachmentsInner.md) | 25 MB in total; 3 MB per attachment on Microsoft. |  [optional] |
|**headers** | **Map&lt;String, String&gt;** | Custom &#x60;X-&#x60; headers only. &#x60;List-Unsubscribe&#x60; is dropped on Microsoft and reported in &#x60;metadata.droppedHeaders&#x60;. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |
|**scheduledFor** | **OffsetDateTime** | Send later, between 1 minute and 30 days from now. The request answers 202 with the scheduled send; it leaves within a minute of this time through the same caps as an immediate send. List or cancel it under &#x60;/v1/email/messages/scheduled&#x60;. |  [optional] |
|**holdAsDraft** | **Boolean** | Reserved; currently rejected. |  [optional] |
|**trackOpens** | **Boolean** | Adds an open pixel to the html and fires &#x60;email.opened&#x60;. Needs &#x60;html&#x60;. |  [optional] |
|**trackLinks** | **Boolean** | Rewrites every http(s) link in the html through a Zernio redirect and fires &#x60;email.link_clicked&#x60;. Needs &#x60;html&#x60;. |  [optional] |
|**trackReplies** | **Boolean** | Fires &#x60;email.thread_replied&#x60; when someone else writes in this message&#39;s thread. Works with text or html. |  [optional] |



