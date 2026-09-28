

# SendRcsMessageRequest

Send exactly one of text or content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentId** | **String** |  |  |
|**to** | **String** | Recipient number (E.164; formatting is normalized). |  |
|**text** | **String** |  |  [optional] |
|**content** | [**RcsContent**](RcsContent.md) |  |  [optional] |
|**fallbackText** | **String** |  |  [optional] |
|**ttlSeconds** | **Integer** | Seconds before an undelivered message expires. |  [optional] |



