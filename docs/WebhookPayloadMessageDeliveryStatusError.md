

# WebhookPayloadMessageDeliveryStatusError

Populated only on message.failed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**details** | **String** | Platform&#39;s extended detail for &#x60;code&#x60; (WhatsApp: Meta&#39;s &#x60;error_data.details&#x60;), when the platform sent one. Absent on SMS. |  [optional] |
|**href** | **URI** | Link to the platform&#39;s documentation for &#x60;code&#x60;, when the platform sent one. |  [optional] |
|**explanation** | **String** | Plain-language translation of &#x60;code&#x60; (e.g. for 131026, that the recipient has likely opted out of marketing messages while utility templates are unaffected, or for 131031, that Meta restricted the WhatsApp Business Account). Null for unmapped codes; fall back to title/message.  |  [optional] |



