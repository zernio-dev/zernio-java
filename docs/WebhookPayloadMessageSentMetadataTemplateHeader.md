

# WebhookPayloadMessageSentMetadataTemplateHeader

WhatsApp template sends only. The header as the recipient saw it: a text header filled with the values actually sent, a media header with its format and the link the send gave, or a location header with only its format.  Absent when the template has no header, and on bulk, broadcast and automation sends, which carry only `templateName` and `templateLanguage`. The message text is the body only. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**format** | [**FormatEnum**](#FormatEnum) | Header format. |  |
|**text** | **String** | Text headers only. The header text with its variables filled in. |  [optional] |
|**mediaUrl** | **String** | Image, video and document headers only. The link the send carried. Absent when the media was sent by id or the link is on Meta&#39;s CDN (an expiring URL, such as the approval sample). |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| DOCUMENT | &quot;document&quot; |
| LOCATION | &quot;location&quot; |



