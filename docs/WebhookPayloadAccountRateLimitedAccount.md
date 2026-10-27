

# WebhookPayloadAccountRateLimitedAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**profileId** | **String** |  |  |
|**platform** | **String** |  |  |
|**username** | **String** |  |  |
|**displayName** | **String** |  |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  |
|**cooldownMinutes** | **Integer** |  |  |
|**resetsAt** | **OffsetDateTime** |  |  |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| RECIPIENT_BURST | &quot;recipient_burst&quot; |
| PROVIDER_REJECTION | &quot;provider_rejection&quot; |
| BOUNCES | &quot;bounces&quot; |
| DAILY_CAP | &quot;daily_cap&quot; |



