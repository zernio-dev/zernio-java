

# UpdateAdStatus200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**updated** | **Integer** | 1 when the switch was written, 0 when skipped |  [optional] |
|**skipped** | **Integer** | 1 when skipped (terminal status, or the ad&#39;s own switch already in the target state), else 0 |  [optional] |
|**status** | **String** | The ad&#39;s delivery status after the call, as the platform reports it when it can be read back (e.g. &#x60;paused&#x60; for an ad switched on under a paused campaign) |  [optional] |
|**configuredStatus** | **String** | The ad&#39;s own on/off switch (&#x60;ACTIVE&#x60; / &#x60;PAUSED&#x60;), re-read from the platform after the write. Null where the platform exposes no per-ad switch (X) or the read-back failed and the platform does not store one. |  [optional] |
|**message** | **String** | Human-readable summary (present only when skipped), e.g. \&quot;No change: the ad&#39;s own switch is already off\&quot; |  [optional] |



