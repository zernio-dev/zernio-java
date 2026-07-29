

# SendInboxMessage400ResponsePlatformError

Instagram/Facebook only. Meta's own diagnostic fields for the rejected send, passed through verbatim so you can tell failure classes apart and quote them to Meta. Absent when the failure did not come from Meta.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | Meta error code |  [optional] |
|**subcode** | **Integer** | Meta error_subcode |  [optional] |
|**fbtraceId** | **String** | Meta fbtrace_id, quote this in a Meta bug report |  [optional] |
|**type** | **String** | Meta error type (e.g. OAuthException) |  [optional] |



