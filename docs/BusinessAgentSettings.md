

# BusinessAgentSettings

Meta Business Agent settings for one WhatsApp number, as Meta returns them.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentId** | **String** |  |  |
|**channel** | **String** |  |  |
|**rollout** | [**BusinessAgentSettingsRollout**](BusinessAgentSettingsRollout.md) |  |  |
|**handoff** | [**BusinessAgentSettingsHandoff**](BusinessAgentSettingsHandoff.md) |  |  [optional] |
|**followup** | [**BusinessAgentSettingsFollowup**](BusinessAgentSettingsFollowup.md) |  |  [optional] |
|**aiAudience** | [**AiAudienceEnum**](#AiAudienceEnum) | EVERYONE answers all consumers; ALLOWLISTED_ONLY answers only the allowlist and needs no payment method. |  [optional] |
|**neverSayPhrases** | **List&lt;String&gt;** | Exact phrases the agent must never say. |  [optional] |



## Enum: AiAudienceEnum

| Name | Value |
|---- | -----|
| EVERYONE | &quot;EVERYONE&quot; |
| ALLOWLISTED_ONLY | &quot;ALLOWLISTED_ONLY&quot; |



