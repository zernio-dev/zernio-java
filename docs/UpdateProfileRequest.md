

# UpdateProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**description** | **String** | Set to null to clear the description. |  [optional] |
|**color** | **String** |  |  [optional] |
|**timezone** | **String** | IANA timezone new posts on this profile use when they name no &#x60;timezone&#x60;. Set to null to go back to UTC. An unknown name returns 400. |  [optional] |
|**externalId** | **String** | Your own identifier for this profile (1 to 255 characters, trimmed). Set to null to clear it. A value another profile of the same owner already holds returns 409 profile_external_id_conflict. |  [optional] |
|**isDefault** | **Boolean** |  |  [optional] |
|**contentRetention** | [**ContentRetentionEnum**](#ContentRetentionEnum) | Turns zero content retention on (&#x60;none&#x60;) or off (&#x60;standard&#x60;) for this profile only, for new data within about a minute. Only the team owner can change it. &#x60;standard&#x60; answers 409 while the whole team has it on; &#x60;none&#x60; answers 409 during a WhatsApp verification of a number of this profile. |  [optional] |
|**maxOutboundCallsPerHour** | **Integer** | Caps outbound calls from this profile&#39;s numbers per rolling hour, inside the team limits. Null clears it. |  [optional] |
|**maxDailyCallSpendUsd** | **BigDecimal** | Caps billed call spend (USD) from this profile&#39;s numbers per rolling 24 hours, inside the team limits. Null clears it. |  [optional] |
|**maxForwardedMinutesPerDay** | **Integer** | Caps minutes forwarded to a phone from this profile&#39;s numbers per rolling 24 hours, inside the team limits. Null clears it. |  [optional] |



## Enum: ContentRetentionEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;standard&quot; |
| NONE | &quot;none&quot; |



