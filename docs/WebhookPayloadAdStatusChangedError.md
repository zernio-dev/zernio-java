

# WebhookPayloadAdStatusChangedError

Optional. Present on most `WITH_ISSUES` events, carrying the platform's error diagnostics. May be absent on some `WITH_ISSUES` events (Meta does not always include diagnostics). Always absent for any other `status.raw` value. Always null-check before reading. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Platform-native error code, forwarded verbatim. For Meta this is &#x60;error_code&#x60; as a string. Use as the stable discriminator — &#x60;summary&#x60; and &#x60;message&#x60; are localized.  |  |
|**summary** | **String** | Short human-readable summary (Meta &#x60;error_summary&#x60;). Localized to the ad-account owner&#39;s Meta locale — display only, do not match on it.  |  [optional] |
|**message** | **String** | Full human-readable error message (Meta &#x60;error_message&#x60;). Localized — display only.  |  [optional] |



