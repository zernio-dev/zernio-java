

# BusinessAgentSkill


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | Lowercase letters, digits and hyphens, e.g. greeting-skill. |  [optional] |
|**description** | **String** | When the agent should apply the skill. |  [optional] |
|**skill** | **String** | The instructions themselves. Avoid two skills that both claim priority for the same situation. |  |
|**id** | **String** |  |  |
|**channel** | **String** |  |  [optional] |
|**createdAt** | **Integer** | Unix seconds. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | pending_review right after a write; blocked means Meta content review rejected it and the agent never applies it. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PENDING_REVIEW | &quot;pending_review&quot; |
| BLOCKED | &quot;blocked&quot; |



