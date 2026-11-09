

# WebhookEmailTrackedMessage

The tracked message an email.* event is about. `messageId` and `threadId` are the provider ids (read the message with `GET /v1/email/messages/{messageId}`); `metadata` is what you sent with it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageId** | **String** |  |  [optional] |
|**threadId** | **String** |  |  [optional] |
|**trackingId** | **String** | Also returned as &#x60;data.trackingId&#x60; by the send. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |



