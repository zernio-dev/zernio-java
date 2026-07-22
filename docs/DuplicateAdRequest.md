

# DuplicateAdRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSetId** | **String** | Destination platform ad set id (defaults to the source&#39;s ad set) |  [optional] |
|**statusOption** | [**StatusOptionEnum**](#StatusOptionEnum) |  |  [optional] |
|**renameStrategy** | [**RenameStrategyEnum**](#RenameStrategyEnum) |  |  [optional] |
|**renamePrefix** | **String** |  |  [optional] |
|**renameSuffix** | **String** |  |  [optional] |
|**syncAfter** | **Boolean** |  |  [optional] |



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



