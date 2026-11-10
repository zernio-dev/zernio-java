

# ForwardEmailRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**to** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  |
|**cc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**bcc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**replyTo** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**fromName** | **String** |  |  [optional] |
|**from** | **String** | Send from another address of the mailbox, as on &#x60;POST /v1/email/messages&#x60;. |  [optional] |
|**appendSignature** | **Boolean** | Gmail only. Appends the signature of the sending address to the note. Outlook answers 400. |  [optional] |
|**subject** | **String** | Defaults to \&quot;Fwd: \&quot; plus the original subject. |  [optional] |
|**text** | **String** | Optional note above the forwarded mail. |  [optional] |
|**html** | **String** | Optional note above the forwarded mail, as html. |  [optional] |
|**attachments** | [**List&lt;EmailAttachmentInput&gt;**](EmailAttachmentInput.md) | Added to the forwarded attachments. Everything together stays under 25 MB, else 413 &#x60;attachment_too_large&#x60;. |  [optional] |
|**includeAttachments** | **Boolean** | False keeps only the inline images of the original. |  [optional] |
|**excludeAttachmentIds** | **List&lt;String&gt;** | Attachment ids (from a read of the original) to leave out. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |
|**trackOpens** | **Boolean** | Adds an open pixel to the note and fires &#x60;email.opened&#x60;. Needs &#x60;html&#x60;. |  [optional] |
|**trackLinks** | **Boolean** | Rewrites the links of the note and fires &#x60;email.link_clicked&#x60;. Needs &#x60;html&#x60;. |  [optional] |
|**trackReplies** | **Boolean** | Fires &#x60;email.thread_replied&#x60; when someone else writes in the thread. |  [optional] |



