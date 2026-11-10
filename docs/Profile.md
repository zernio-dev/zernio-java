

# Profile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**userId** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**color** | **String** |  |  [optional] |
|**timezone** | **String** | IANA timezone new posts on this profile use when the request names no &#x60;timezone&#x60;. Null means UTC. |  [optional] |
|**externalId** | **String** | Your own identifier for this profile, set on create or update. Null when none is set. |  [optional] |
|**contentRetention** | [**ContentRetentionEnum**](#ContentRetentionEnum) | This profile&#39;s own zero content retention setting. &#x60;none&#x60; stores identifiers and metadata only for this profile. Change it with &#x60;contentRetention&#x60; on update; only the team owner can. |  [optional] |
|**effectiveContentRetention** | [**EffectiveContentRetentionEnum**](#EffectiveContentRetentionEnum) | The mode that applies to this profile: &#x60;none&#x60; when the profile or the whole team uses zero content retention. |  [optional] |
|**isDefault** | **Boolean** |  |  [optional] |
|**isOverLimit** | **Boolean** | Only present when includeOverLimit&#x3D;true. Indicates if this profile exceeds the plan limit. |  [optional] |
|**accountCount** | **Integer** | In the profile list. Connected accounts on the profile, including ones that need reconnecting; phone and SMS number internals and posting accounts hidden by an ads connect are not counted. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: ContentRetentionEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;standard&quot; |
| NONE | &quot;none&quot; |



## Enum: EffectiveContentRetentionEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;standard&quot; |
| NONE | &quot;none&quot; |



