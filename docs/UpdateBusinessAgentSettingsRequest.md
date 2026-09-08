

# UpdateBusinessAgentSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rollout** | [**UpdateBusinessAgentSettingsRequestRollout**](UpdateBusinessAgentSettingsRequestRollout.md) |  |  [optional] |
|**handoff** | [**UpdateBusinessAgentSettingsRequestHandoff**](UpdateBusinessAgentSettingsRequestHandoff.md) |  |  [optional] |
|**followup** | [**UpdateBusinessAgentSettingsRequestFollowup**](UpdateBusinessAgentSettingsRequestFollowup.md) |  |  [optional] |
|**aiAudience** | [**AiAudienceEnum**](#AiAudienceEnum) |  |  [optional] |
|**neverSayPhrases** | **List&lt;String&gt;** | Exact phrases the agent must never say; the full replacement list. |  [optional] |



## Enum: AiAudienceEnum

| Name | Value |
|---- | -----|
| EVERYONE | &quot;EVERYONE&quot; |
| ALLOWLISTED_ONLY | &quot;ALLOWLISTED_ONLY&quot; |



