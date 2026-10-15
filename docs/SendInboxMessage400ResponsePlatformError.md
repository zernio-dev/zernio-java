

# SendInboxMessage400ResponsePlatformError

Instagram, Facebook, WhatsApp, or TikTok. The platform's diagnostic fields for the rejected send or template lookup. WhatsApp lookup errors retain only code, message, and error_data.details. On TikTok only code, message, and request_id are set. Absent when the failure did not come from the platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | Meta or TikTok error code |  [optional] |
|**subcode** | **Integer** | Meta error_subcode |  [optional] |
|**fbtraceId** | **String** | Meta fbtrace_id, quote this in a Meta bug report |  [optional] |
|**type** | **String** | Meta error type (e.g. OAuthException) |  [optional] |
|**message** | **String** | TikTok error message |  [optional] |
|**requestId** | **String** | TikTok request_id, quote this in a TikTok support ticket |  [optional] |



