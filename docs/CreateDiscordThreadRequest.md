

# CreateDiscordThreadRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Thread name |  |
|**messageId** | **String** | Optional message snowflake to start the thread from. Omit for a standalone thread. |  [optional] |
|**autoArchiveDuration** | [**AutoArchiveDurationEnum**](#AutoArchiveDurationEnum) | Minutes of inactivity before the thread auto-archives. Discord accepts only these four values. |  [optional] |



## Enum: AutoArchiveDurationEnum

| Name | Value |
|---- | -----|
| NUMBER_60 | 60 |
| NUMBER_1440 | 1440 |
| NUMBER_4320 | 4320 |
| NUMBER_10080 | 10080 |



