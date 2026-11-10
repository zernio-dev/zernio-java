

# WebhookPayloadEmailBouncedEmail

The mail that bounced. `messageId`, `trackingId` and `metadata` are set when it was sent with tracking; otherwise match on `threadId`, `internetMessageId` or `subject`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageId** | **String** | Provider id of the sent mail. |  [optional] |
|**threadId** | **String** |  |  [optional] |
|**internetMessageId** | **String** | The RFC 5322 Message-ID of the mail that bounced. |  [optional] |
|**trackingId** | **String** |  |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |
|**subject** | **String** | From the headers the report quotes. |  [optional] |
|**sentAt** | **OffsetDateTime** | From the headers the report quotes. |  [optional] |



