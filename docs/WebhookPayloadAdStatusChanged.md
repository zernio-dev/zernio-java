

# WebhookPayloadAdStatusChanged

Webhook payload for the `ad.status_changed` event. Currently emitted only for Meta (`metaads`).  Sourced from two Meta `ad_account` webhook fields:   - `in_process_ad_objects` - the ad object finished processing and     exited `IN_PROCESS`. `status.raw` carries Meta's `status_name`.   - `with_issues_ad_objects` - the ad object entered `WITH_ISSUES`.     `status.raw` is `WITH_ISSUES` and the `error` block is populated     from Meta's `error_code` / `error_summary` / `error_message`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable webhook event ID |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**account** | [**WebhookPayloadAdStatusChangedAccount**](WebhookPayloadAdStatusChangedAccount.md) |  |  |
|**adObject** | [**WebhookPayloadAdStatusChangedAdObject**](WebhookPayloadAdStatusChangedAdObject.md) |  |  |
|**status** | [**WebhookPayloadAdStatusChangedStatus**](WebhookPayloadAdStatusChangedStatus.md) |  |  |
|**error** | [**WebhookPayloadAdStatusChangedError**](WebhookPayloadAdStatusChangedError.md) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | ISO-8601 timestamp the webhook was produced. |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| AD_STATUS_CHANGED | &quot;ad.status_changed&quot; |



