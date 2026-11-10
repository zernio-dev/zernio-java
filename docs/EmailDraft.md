

# EmailDraft

A draft in the mailbox. Carries the message fields; `id` is the draft id the drafts endpoints take. Store `id`, not `messageId`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The draft id: the Gmail draft id, or the Outlook message id. |  [optional] |
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
|**labels** | **List&lt;String&gt;** | Gmail: the ids of the user labels on the message (names come from &#x60;GET /v1/email/labels&#x60;). Outlook: its category names. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |
|**trackingId** | **String** | Set when the draft was created with tracking. |  [optional] |
|**clean** | [**EmailClean**](EmailClean.md) |  |  [optional] |
|**draftId** | **String** | On a mail sent from a draft (&#x60;POST /v1/email/drafts/{draftId}/send&#x60;): the draft it was. The sent mail has a new id. |  [optional] |
|**forwardedFrom** | **String** | On a forward: the message it forwarded. |  [optional] |
|**_object** | [**ObjectEnum**](#ObjectEnum) |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Fixed when the draft is created. A draft the user wrote in their mail client is read from its headers. |  [optional] |
|**version** | **String** | Changes on every edit, the user&#39;s in Gmail or Outlook included. Pass it as &#x60;If-Match&#x60; to update or send only that version. Also the &#x60;ETag&#x60; response header. |  [optional] |
|**messageId** | **String** | The provider message behind the draft. Volatile: Gmail replaces it on every save. |  [optional] |
|**inReplyTo** | **String** | The message a reply draft answers. |  [optional] |
|**forwardOf** | **String** | The message a forward draft forwards. |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |



## Enum: ObjectEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| NEW | &quot;new&quot; |
| REPLY | &quot;reply&quot; |
| FORWARD | &quot;forward&quot; |



