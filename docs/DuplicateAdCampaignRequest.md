

# DuplicateAdCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**deepCopy** | **Boolean** | Copy child ad sets + ads + creatives + targeting |  [optional] |
|**statusOption** | [**StatusOptionEnum**](#StatusOptionEnum) | ACTIVE &#x3D; launch the clone immediately (spends the moment LinkedIn approves it). PAUSED &#x3D; clone stays DRAFT, safe default. INHERITED_FROM_SOURCE &#x3D; mirror each entity&#39;s source status per-entity. Duplicating an ACTIVE campaign this way starts a second front of spend.  |  [optional] |
|**startTime** | **OffsetDateTime** | Reschedule the copied hierarchy&#39;s start (ISO 8601). On Meta and TikTok a value without an offset (&#x60;YYYY-MM-DD&#x60;, &#x60;YYYY-MM-DD HH:MM:SS&#x60; or &#x60;YYYY-MM-DDTHH:MM:SS&#x60;) is read in the ad account timezone; LinkedIn ad accounts carry no timezone, so there it is read as UTC. TikTok defaults to a start a few minutes after the copy. |  [optional] |
|**endTime** | **OffsetDateTime** | Reschedule the copied hierarchy&#39;s end, read like &#x60;startTime&#x60;; a date-only end runs to 23:59:59 local. Defaults to the source&#39;s end. |  [optional] |
|**renameStrategy** | [**RenameStrategyEnum**](#RenameStrategyEnum) |  |  [optional] |
|**renamePrefix** | **String** |  |  [optional] |
|**renameSuffix** | **String** |  |  [optional] |
|**syncAfter** | **Boolean** | Trigger ads discovery on the owning account after the copy succeeds |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| TIKTOK | &quot;tiktok&quot; |
| LINKEDIN | &quot;linkedin&quot; |



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



