

# SendInboxMessage400Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | **String** |  |  [optional] |
|**code** | [**CodeEnum**](#CodeEnum) | Stable machine-readable reason. PLATFORM_LIMITATION covers a capability the platform does not offer (e.g. Bluesky and Reddit DMs reject media); MISSING_PARTICIPANT means the stored conversation has no recipient to send to. |  [optional] |
|**platformError** | [**SendInboxMessage400ResponsePlatformError**](SendInboxMessage400ResponsePlatformError.md) |  |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| PLATFORM_LIMITATION | &quot;PLATFORM_LIMITATION&quot; |
| MISSING_PARTICIPANT | &quot;MISSING_PARTICIPANT&quot; |



