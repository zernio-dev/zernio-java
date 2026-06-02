

# UpdateDiscordScheduledEventRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**startsAt** | **OffsetDateTime** |  |  [optional] |
|**endsAt** | **OffsetDateTime** |  |  [optional] |
|**location** | **String** | For external events. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status transition. Most common: &#39;cancelled&#39; to cancel an event. |  [optional] |
|**imageDataUri** | **String** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SCHEDULED | &quot;scheduled&quot; |
| ACTIVE | &quot;active&quot; |
| COMPLETED | &quot;completed&quot; |
| CANCELLED | &quot;cancelled&quot; |



