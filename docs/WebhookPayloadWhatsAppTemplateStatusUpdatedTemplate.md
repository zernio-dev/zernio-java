

# WebhookPayloadWhatsAppTemplateStatusUpdatedTemplate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**templateId** | **String** | Meta&#39;s &#x60;message_template_id&#x60;, returned as a string. |  |
|**name** | **String** | Meta&#39;s &#x60;message_template_name&#x60;. |  |
|**language** | **String** | Meta&#39;s &#x60;message_template_language&#x60; (e.g. &#x60;en_US&#x60;). |  |
|**status** | [**StatusEnum**](#StatusEnum) | New status. Forwarded verbatim from Meta&#39;s &#x60;event&#x60; field. &#x60;PENDING_DELETION&#x60; is the 24h-grace state after a delete request before the template is actually removed.  |  |
|**reason** | **String** | Meta&#39;s free-form reason for the transition. &#x60;\&quot;NONE\&quot;&#x60; on approval; an explanation string on rejection.  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;APPROVED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| PENDING | &quot;PENDING&quot; |
| PAUSED | &quot;PAUSED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| IN_APPEAL | &quot;IN_APPEAL&quot; |
| PENDING_DELETION | &quot;PENDING_DELETION&quot; |



