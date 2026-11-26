

# AutomationGraph

An automation's definition as one graph: the trigger that starts it, the nodes its runs walk from `entry` along `edges`, and its guardrails. Ad rules, event and scheduled automations and sequences run their nodes in one chain, a condition first where the kind has one.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**triggers** | [**List&lt;AutomationGraphTriggersInner&gt;**](AutomationGraphTriggersInner.md) | One trigger. Its &#x60;type&#x60; is the kind&#39;s &#x60;trigger.type&#x60;; &#x60;config&#x60; holds the rest of the trigger, and &#x60;subjects&#x60; for a schedule. |  |
|**nodes** | [**List&lt;AutomationGraphNodesInner&gt;**](AutomationGraphNodesInner.md) |  |  |
|**edges** | [**List&lt;AutomationGraphEdgesInner&gt;**](AutomationGraphEdgesInner.md) |  |  |
|**entry** | **List&lt;String&gt;** | The node runs start at. |  |
|**limits** | [**AutomationGraphLimits**](AutomationGraphLimits.md) |  |  |



