

# CreateBroadcastRequestMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**text** | **String** | Required on every platform except WhatsApp (which sends &#x60;template&#x60;) and an SMS broadcast that carries attachments. |  [optional] |
|**attachments** | [**List&lt;CreateBroadcastRequestMessageAttachmentsInner&gt;**](CreateBroadcastRequestMessageAttachmentsInner.md) | SMS only: sent as MMS media, one media_url per attachment. Each url must be public http(s); JPEG, PNG, GIF, WEBP, MP4 or 3GPP under 1 MB (checked at create when the host answers a HEAD request; Telnyx enforces the 1 MB total per message at send). |  [optional] |
|**messageTag** | [**MessageTagEnum**](#MessageTagEnum) | Instagram and Facebook only. Meta message tag sent with every recipient message (messaging_type MESSAGE_TAG) so the broadcast can reach people outside the 24h window. Instagram accepts HUMAN_AGENT only. Rejected with a 400 on any other platform. |  [optional] |



## Enum: MessageTagEnum

| Name | Value |
|---- | -----|
| CONFIRMED_EVENT_UPDATE | &quot;CONFIRMED_EVENT_UPDATE&quot; |
| POST_PURCHASE_UPDATE | &quot;POST_PURCHASE_UPDATE&quot; |
| ACCOUNT_UPDATE | &quot;ACCOUNT_UPDATE&quot; |
| HUMAN_AGENT | &quot;HUMAN_AGENT&quot; |



