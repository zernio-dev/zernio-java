

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
|**reuseSourceCreative** | **Boolean** | Point the copy at the source ad&#39;s creative object instead of copying it, so the copy keeps the same Facebook post, the same Instagram media, their existing likes, comments and shares, and the full creative setup (text variations included). This is what Ads Manager&#39;s \&quot;show existing reactions, comments and shares\&quot; does. Meta&#39;s native copy always publishes new posts. A creative belongs to one ad account, so &#x60;adSetId&#x60; must be in the source ad&#39;s account. 400 when the source ad has no creative yet. |  [optional] |



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



