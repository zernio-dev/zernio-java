

# WebhookPayloadAdAccountStatusChangedStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**previous** | [**PreviousEnum**](#PreviousEnum) |  |  |
|**current** | [**CurrentEnum**](#CurrentEnum) |  |  |
|**raw** | **String** | Platform-native status, forwarded verbatim (Meta &#x60;account_status&#x60; code such as &#x60;2&#x60;, Google &#x60;SUSPENDED&#x60;, TikTok &#x60;STATUS_LIMIT&#x60;, X &#x60;REJECTED&#x60;). |  |



## Enum: PreviousEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| RESTRICTED | &quot;restricted&quot; |
| DISABLED | &quot;disabled&quot; |
| CLOSED | &quot;closed&quot; |



## Enum: CurrentEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| RESTRICTED | &quot;restricted&quot; |
| DISABLED | &quot;disabled&quot; |
| CLOSED | &quot;closed&quot; |



