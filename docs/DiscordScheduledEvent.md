

# DiscordScheduledEvent

Discord guild scheduled event. Returned by /v1/discord/guilds/{guildId}/events endpoints. Fields below are the subset Zernio consumes — Discord may return more (e.g. creator, image hash) which we pass through verbatim. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Event snowflake ID |  [optional] |
|**guildId** | **String** |  |  [optional] |
|**channelId** | **String** | Voice/stage channel ID; null for external events. |  [optional] |
|**creatorId** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**scheduledStartTime** | **OffsetDateTime** |  |  [optional] |
|**scheduledEndTime** | **OffsetDateTime** | Required for external events; optional for voice/stage. |  [optional] |
|**privacyLevel** | [**PrivacyLevelEnum**](#PrivacyLevelEnum) | Always 2 (GUILD_ONLY) — Discord deprecated PUBLIC events. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | 1&#x3D;SCHEDULED, 2&#x3D;ACTIVE, 3&#x3D;COMPLETED, 4&#x3D;CANCELED |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | 1&#x3D;STAGE_INSTANCE, 2&#x3D;VOICE, 3&#x3D;EXTERNAL |  [optional] |
|**entityId** | **String** |  |  [optional] |
|**entityMetadata** | [**DiscordScheduledEventEntityMetadata**](DiscordScheduledEventEntityMetadata.md) |  |  [optional] |
|**userCount** | **Integer** | Number of members who RSVP&#39;d. Only present when withUserCount&#x3D;true on list. |  [optional] |
|**image** | **String** | Cover image hash; build URL via cdn.discordapp.com. |  [optional] |



## Enum: PrivacyLevelEnum

| Name | Value |
|---- | -----|
| NUMBER_2 | 2 |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



