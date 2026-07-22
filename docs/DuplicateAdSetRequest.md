

# DuplicateAdSetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**campaignId** | **String** | Destination platform campaign id (defaults to the source&#39;s campaign) |  [optional] |
|**deepCopy** | **Boolean** | Copy child ads + creatives |  [optional] |
|**statusOption** | [**StatusOptionEnum**](#StatusOptionEnum) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Reschedule the copy&#39;s start time |  [optional] |
|**endTime** | **OffsetDateTime** |  |  [optional] |
|**renameStrategy** | [**RenameStrategyEnum**](#RenameStrategyEnum) |  |  [optional] |
|**renamePrefix** | **String** |  |  [optional] |
|**renameSuffix** | **String** |  |  [optional] |
|**syncAfter** | **Boolean** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |



## Enum: StatusOptionEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PAUSED | &quot;PAUSED&quot; |
| INHERITED_FROM_SOURCE | &quot;INHERITED_FROM_SOURCE&quot; |



## Enum: RenameStrategyEnum

| Name | Value |
|---- | -----|
| DEEP_RENAME | &quot;DEEP_RENAME&quot; |
| ONLY_TOP_LEVEL_RENAME | &quot;ONLY_TOP_LEVEL_RENAME&quot; |
| NO_RENAME | &quot;NO_RENAME&quot; |



