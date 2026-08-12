

# LinkedInPlatformDataPoll

Create a LinkedIn poll with this post. Cannot be combined with media or reshareUrl. Polls cannot be edited after publishing on LinkedIn, and API-created polls are non-sponsored only (they cannot be promoted as ads).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**question** | **String** | Poll question (max 140 characters) |  |
|**options** | **List&lt;String&gt;** | Poll options (2-4 choices, max 30 characters each) |  |
|**duration** | [**DurationEnum**](#DurationEnum) | How long the poll accepts votes. Defaults to SEVEN_DAYS. |  [optional] |



## Enum: DurationEnum

| Name | Value |
|---- | -----|
| ONE_DAY | &quot;ONE_DAY&quot; |
| THREE_DAYS | &quot;THREE_DAYS&quot; |
| SEVEN_DAYS | &quot;SEVEN_DAYS&quot; |
| FOURTEEN_DAYS | &quot;FOURTEEN_DAYS&quot; |



