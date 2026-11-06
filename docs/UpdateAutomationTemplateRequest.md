

# UpdateAutomationTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | [**AutomationTemplateContentFrom**](AutomationTemplateContentFrom.md) |  |  [optional] |
|**automations** | [**List&lt;AutomationDefinition&gt;**](AutomationDefinition.md) | Automation definitions, each checked like a &#x60;POST /v1/automations&#x60; body. Ad accounts, a trigger&#39;s profile and accounts, and alert destinations become inputs. |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) |  |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| TEAM | &quot;team&quot; |
| LINK | &quot;link&quot; |



