

# DuplicateAdSetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**campaignId** | **String** | Destination platform campaign id (defaults to the source&#39;s campaign) |  [optional] |
|**deepCopy** | **Boolean** | Copy child ads + creatives |  [optional] |
|**statusOption** | [**StatusOptionEnum**](#StatusOptionEnum) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Reschedule the copy&#39;s start (ISO 8601). A value without an offset (&#x60;YYYY-MM-DD&#x60;, &#x60;YYYY-MM-DD HH:MM:SS&#x60; or &#x60;YYYY-MM-DDTHH:MM:SS&#x60;) is read in the ad account timezone. |  [optional] |
|**endTime** | **OffsetDateTime** | Reschedule the copy&#39;s end, read like &#x60;startTime&#x60;; a date-only end runs to 23:59:59 local. |  [optional] |
|**renameStrategy** | [**RenameStrategyEnum**](#RenameStrategyEnum) | Meta&#39;s native &#x60;rename_strategy&#x60; values. &#x60;DEEP_RENAME&#x60; renames the copied ad set and its copied ads with &#x60;renamePrefix&#x60; / &#x60;renameSuffix&#x60;. &#x60;ONLY_TOP_LEVEL_RENAME&#x60; renames only the copied ad set; its ads keep their source names. &#x60;NO_RENAME&#x60; keeps every source name. With no rename option at all, Meta appends its own &#x60; - Copy&#x60; suffix. Ignored on TikTok, where &#x60;renamePrefix&#x60; / &#x60;renameSuffix&#x60; still apply. |  [optional] |
|**renamePrefix** | **String** | Text prepended to each renamed object&#39;s name. |  [optional] |
|**renameSuffix** | **String** | Text appended to each renamed object&#39;s name. |  [optional] |
|**syncAfter** | **Boolean** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| TIKTOK | &quot;tiktok&quot; |



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



