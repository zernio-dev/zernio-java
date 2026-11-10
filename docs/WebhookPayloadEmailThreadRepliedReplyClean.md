

# WebhookPayloadEmailThreadRepliedReplyClean

The reply without the quoted history, as `clean=true` returns it on a message read. `status: fallback` means nothing could be stripped safely and `text` is the whole body.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**text** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STRIPPED | &quot;stripped&quot; |
| UNCHANGED | &quot;unchanged&quot; |
| FALLBACK | &quot;fallback&quot; |



