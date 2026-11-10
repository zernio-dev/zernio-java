

# CreateEmailDraftRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**to** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) | Optional on a draft; needed before it is sent. |  [optional] |
|**cc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**bcc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**replyTo** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**fromName** | **String** |  |  [optional] |
|**from** | **String** | Send from another address of the mailbox, as on &#x60;POST /v1/email/messages&#x60;. Checked when the draft is saved. |  [optional] |
|**appendSignature** | **Boolean** | Puts the signature of the sending address in the draft body, where the user sees it: its Zernio default first, else its Gmail signature. |  [optional] |
|**signatureId** | **String** | Puts this Zernio signature in the draft body instead. Wins over &#x60;appendSignature&#x60;. |  [optional] |
|**subject** | **String** | On a reply draft, empty keeps the thread subject. |  [optional] |
|**text** | **String** |  |  [optional] |
|**html** | **String** |  |  [optional] |
|**attachments** | [**List&lt;EmailAttachmentInput&gt;**](EmailAttachmentInput.md) |  |  [optional] |
|**headers** | **Map&lt;String, String&gt;** | Custom &#x60;X-&#x60; headers only. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Kept with the draft and returned on the sent message and its email.* webhooks. |  [optional] |
|**inReplyTo** | **String** | Makes a reply draft in that message&#39;s thread, addressed and threaded like a reply. Not with &#x60;forwardOf&#x60;. |  [optional] |
|**replyAll** | **Boolean** | With &#x60;inReplyTo&#x60;: address every recipient of the original. Leave out &#x60;to&#x60;, &#x60;cc&#x60; and &#x60;bcc&#x60;. |  [optional] |
|**forwardOf** | **String** | Makes a forward draft of that message, with its attachments. Recipients can come later. Not with &#x60;inReplyTo&#x60;. |  [optional] |
|**includeAttachments** | **Boolean** | With &#x60;forwardOf&#x60;: false keeps only the inline images of the original. |  [optional] |
|**excludeAttachmentIds** | **List&lt;String&gt;** | With &#x60;forwardOf&#x60;: attachment ids (from a read of the original) to leave out. |  [optional] |
|**trackOpens** | **Boolean** | Puts the open pixel in the draft html now; fires &#x60;email.opened&#x60; once it is sent. Needs &#x60;html&#x60;. |  [optional] |
|**trackLinks** | **Boolean** | Rewrites the draft&#39;s links now; fires &#x60;email.link_clicked&#x60; once it is sent. Needs &#x60;html&#x60;. |  [optional] |
|**trackReplies** | **Boolean** | Fires &#x60;email.thread_replied&#x60; once it is sent. |  [optional] |



