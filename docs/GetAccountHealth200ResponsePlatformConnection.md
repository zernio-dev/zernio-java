

# GetAccountHealth200ResponsePlatformConnection

WhatsApp accounts only. Live probe of the Meta link behind the channel, performed at request time (the same read as GET /v1/whatsapp/number-info).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;connected&#x60; &#x3D; Meta served the channel object. &#x60;disconnected&#x60; &#x3D; Meta refused to serve it (Graph error 100, subcode 33), which is how a phone-side coexistence disconnect surfaces. &#x60;unknown&#x60; &#x3D; the live read failed for another reason (timeout, transient Meta error), not evidence either way. |  [optional] |
|**checkedAt** | **OffsetDateTime** | When this live probe ran (always the current request; never cached) |  [optional] |
|**phoneStatus** | **String** | Meta&#39;s own &#x60;status&#x60; field from the phone-number node (for example CONNECTED), when the object was readable |  [optional] |
|**metaError** | [**GetAccountHealth200ResponsePlatformConnectionMetaError**](GetAccountHealth200ResponsePlatformConnectionMetaError.md) |  |  [optional] |
|**inboundWebhookSubscribed** | **Boolean** | From the phone number&#39;s Meta health_status, overridden to &#x60;false&#x60; when subscribing the number&#39;s WhatsApp Business Account to Zernio&#39;s webhooks failed at connect.  - &#x60;false&#x60;: Meta says Zernio is not subscribed to the message webhook for this number, or the subscribe failed when the number was connected, so inbound messages are not delivered, though the number is CONNECTED and can still send. - &#x60;false&#x60;, fix: re-subscribe (reconnect the number). If it stays &#x60;false&#x60;, the number is routed to a different WhatsApp Business Account (typically after linking it to a Facebook Page). - &#x60;true&#x60;: Meta reports no such problem. - &#x60;null&#x60;: Meta did not report it (read failed or no health_status); not evidence either way.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CONNECTED | &quot;connected&quot; |
| DISCONNECTED | &quot;disconnected&quot; |
| UNKNOWN | &quot;unknown&quot; |



