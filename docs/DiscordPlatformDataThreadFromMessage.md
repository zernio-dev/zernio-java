

# DiscordPlatformDataThreadFromMessage

Create a follow-up thread under the published message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Thread name (1-100 chars) |  [optional] |
|**autoArchiveDuration** | [**AutoArchiveDurationEnum**](#AutoArchiveDurationEnum) | Auto-archive after inactivity (minutes) |  [optional] |
|**rateLimitPerUser** | **Integer** | Slow-mode duration in seconds (0-21600) |  [optional] |



## Enum: AutoArchiveDurationEnum

| Name | Value |
|---- | -----|
| NUMBER_60 | 60 |
| NUMBER_1440 | 1440 |
| NUMBER_4320 | 4320 |
| NUMBER_10080 | 10080 |



