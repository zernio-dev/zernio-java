

# AutomationTemplateContent

Where the automations come from. Send `from` or `automations`, not both.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | [**AutomationTemplateContentFrom**](AutomationTemplateContentFrom.md) |  |  [optional] |
|**automations** | [**List&lt;AutomationDefinition&gt;**](AutomationDefinition.md) | Automation definitions, each checked like a &#x60;POST /v1/automations&#x60; body. Ad accounts, a trigger&#39;s profile and accounts, and alert destinations become inputs. |  [optional] |



