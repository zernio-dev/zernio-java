

# SendInboxMessage400ResponsePlatformError

Instagram, Facebook, or WhatsApp. Meta's diagnostic fields for the rejected send or template lookup. WhatsApp lookup errors retain only code, message, and error_data.details. Absent when the failure did not come from Meta.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | Meta error code |  [optional] |
|**subcode** | **Integer** | Meta error_subcode |  [optional] |
|**fbtraceId** | **String** | Meta fbtrace_id, quote this in a Meta bug report |  [optional] |
|**type** | **String** | Meta error type (e.g. OAuthException) |  [optional] |



