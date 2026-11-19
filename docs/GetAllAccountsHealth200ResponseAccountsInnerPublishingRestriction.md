

# GetAllAccountsHealth200ResponseAccountsInnerPublishingRestriction

Set when the last 3 finished publishes failed with the same account-level error (suspended, restricted, a verification check, an expired login). The next successful publish or a reconnect clears it. While set, status is at least `warning`. Null when the account publishes normally.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  [optional] |
|**message** | **String** | The stored error message of the last failed publish. |  [optional] |
|**since** | **OffsetDateTime** |  |  [optional] |
|**lastFailedAt** | **OffsetDateTime** |  |  [optional] |
|**blocksPublishNow** | **Boolean** | True while POST /v1/posts refuses publish-now posts to this account with 422 &#x60;account_restricted&#x60; (24 hours after the last failure). Scheduled posts are always accepted. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| RESTRICTED | &quot;restricted&quot; |
| SUSPENDED | &quot;suspended&quot; |
| VERIFICATION_REQUIRED | &quot;verification_required&quot; |
| AUTH_EXPIRED | &quot;auth_expired&quot; |



