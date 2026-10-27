

# CreateBroadcastRequestMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**text** | **String** | Required on every platform except WhatsApp (which sends &#x60;template&#x60;) and an SMS broadcast that carries attachments. |  [optional] |
|**attachments** | [**List&lt;CreateBroadcastRequestMessageAttachmentsInner&gt;**](CreateBroadcastRequestMessageAttachmentsInner.md) | SMS only: sent as MMS media, one media_url per attachment. Each url must be public http(s); JPEG, PNG, GIF, WEBP, MP4 or 3GPP under 1 MB (checked at create when the host answers a HEAD request; Telnyx enforces the 1 MB total per message at send). |  [optional] |
|**messageTag** | [**MessageTagEnum**](#MessageTagEnum) | Not usable: a broadcast only reaches people within the 24h window. HUMAN_AGENT is rejected with a 400 because it is only for replies typed by a person, and Meta retired the other tags. |  [optional] |



## Enum: MessageTagEnum

| Name | Value |
|---- | -----|
| CONFIRMED_EVENT_UPDATE | &quot;CONFIRMED_EVENT_UPDATE&quot; |
| POST_PURCHASE_UPDATE | &quot;POST_PURCHASE_UPDATE&quot; |
| ACCOUNT_UPDATE | &quot;ACCOUNT_UPDATE&quot; |
| HUMAN_AGENT | &quot;HUMAN_AGENT&quot; |



