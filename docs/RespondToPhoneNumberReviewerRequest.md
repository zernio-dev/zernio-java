

# RespondToPhoneNumberReviewerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Your message to the reviewer. |  [optional] |
|**documents** | [**List&lt;RespondToPhoneNumberReviewerRequestDocumentsInner&gt;**](RespondToPhoneNumberReviewerRequestDocumentsInner.md) | Corrected requirement documents, each keyed to its requirement. |  [optional] |
|**address** | **Object** | A corrected address record, keyed to its requirement. |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) |  |  [optional] |
|**attachments** | [**List&lt;ReplyToPhoneNumberReviewerRequestAttachmentsInner&gt;**](ReplyToPhoneNumberReviewerRequestAttachmentsInner.md) | Loose files (PDF/JPG/PNG/WEBP, max 10 MB each) whose links are added to your message. |  [optional] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| INDIVIDUAL | &quot;individual&quot; |
| BUSINESS | &quot;business&quot; |



