

# PostPlatformError

The platform's own error for this target, so you can see what the platform said (access tokens are redacted). errorMessage stays the human-readable summary; this block is for diagnostics and support tickets.  **Lifecycle**: set when the last attempt failed with an error the platform described (currently Instagram and Facebook). Kept while an automatic retry of that failure is pending or running; cleared when the target publishes or is retried manually.  **Instagram**:  - Media processing failures carry no code or subcode, only Meta's status text in message. - On a publish whose outcome is uncertain (for example errorMessage starting \"Instagram did not confirm\"), carries the last media_publish error Meta returned, when it returned one. errorMessage stays the verdict, so do not read this block as a confirmed failure. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | Meta error code, when Meta sent one. |  [optional] |
|**subcode** | **Integer** | Meta error_subcode, when Meta sent one. |  [optional] |
|**message** | **String** | The platform&#39;s raw error message or media processing status text. |  |



