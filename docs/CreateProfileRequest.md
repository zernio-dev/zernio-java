

# CreateProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**color** | **String** |  |  [optional] |
|**timezone** | **String** | IANA timezone new posts on this profile use when they name no &#x60;timezone&#x60;. Omit to keep UTC. An unknown name returns 400. |  [optional] |
|**externalId** | **String** | Your own identifier for this profile, typically the id of the tenant or client it serves in your system (1 to 255 characters, trimmed). Unique among the profiles of the user who owns the profile: a duplicate returns 409 profile_external_id_conflict. Look a profile up by it with GET /v1/profiles?externalId&#x3D;. |  [optional] |
|**contentRetention** | [**ContentRetentionEnum**](#ContentRetentionEnum) | Set &#x60;none&#x60; to create the profile with zero content retention, so nothing of its accounts is stored from the first sync. Only the team owner can, with a session or a full-access key; anyone else gets 403. |  [optional] |
|**maxOutboundCallsPerHour** | **Integer** | Caps outbound calls from this profile&#39;s numbers per rolling hour, inside the team limits. Omit for no profile cap. |  [optional] |
|**maxDailyCallSpendUsd** | **BigDecimal** | Caps billed call spend (USD) from this profile&#39;s numbers per rolling 24 hours, inside the team limits. Omit for no profile cap. |  [optional] |
|**maxForwardedMinutesPerDay** | **Integer** | Caps minutes forwarded to a phone from this profile&#39;s numbers per rolling 24 hours, inside the team limits. Omit for no profile cap. |  [optional] |



## Enum: ContentRetentionEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;standard&quot; |
| NONE | &quot;none&quot; |



