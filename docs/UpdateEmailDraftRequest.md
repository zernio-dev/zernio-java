

# UpdateEmailDraftRequest

Every field is optional; the ones you leave out keep their current value. `text` or `html` replaces the whole body, and `attachments` replaces the whole set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**to** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**cc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**bcc** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**replyTo** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**subject** | **String** |  |  [optional] |
|**text** | **String** |  |  [optional] |
|**html** | **String** | On a draft created with tracking, the new html is instrumented again under the same &#x60;trackingId&#x60;. |  [optional] |
|**attachments** | [**List&lt;EmailAttachmentInput&gt;**](EmailAttachmentInput.md) |  |  [optional] |



