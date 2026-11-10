

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
|**labels** | **List&lt;String&gt;** | Gmail: the ids of the user labels on the message (names come from &#x60;GET /v1/email/labels&#x60;). Outlook: its category names. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |
|**trackingId** | **String** | Set on a send with &#x60;trackOpens&#x60;, &#x60;trackLinks&#x60; or &#x60;trackReplies&#x60;; the email.* webhooks carry it. |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |



