

# SendInboxMessage200ResponseDataPartialFailure

Facebook/Instagram only. The attachment was delivered but the follow-up text message was rejected by Meta and was not stored; the response is still a 200 because the attachment send succeeded.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**part** | [**PartEnum**](#PartEnum) |  |  [optional] |
|**error** | **String** |  |  [optional] |
|**platformError** | [**SendInboxMessage200ResponseDataPartialFailurePlatformError**](SendInboxMessage200ResponseDataPartialFailurePlatformError.md) |  |  [optional] |



## Enum: PartEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |



