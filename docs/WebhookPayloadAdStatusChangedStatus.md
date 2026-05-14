

# WebhookPayloadAdStatusChangedStatus

Status info. Branch on `status.raw` to handle each transition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**raw** | **String** | Platform-native status string, forwarded verbatim. For Meta this is &#x60;status_name&#x60; from &#x60;in_process_ad_objects&#x60; (e.g. &#x60;ACTIVE&#x60;, &#x60;PAUSED&#x60;, &#x60;PENDING_REVIEW&#x60;, &#x60;ARCHIVED&#x60;, &#x60;DELETED&#x60;, &#x60;DISAPPROVED&#x60;), or &#x60;WITH_ISSUES&#x60; when sourced from &#x60;with_issues_ad_objects&#x60;. Not constrained by an &#x60;enum&#x60; — Meta may add new values.  |  |



