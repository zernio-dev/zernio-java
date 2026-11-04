

# AdRuleLifecycle

Turns matches into alerts. An object acts and notifies only after `confirmChecks` matching runs in a row; its alert stays open while it matches or `hold` holds, turns critical when `critical` holds, and resolves on its own. Cooldown and caps still decide repeat actions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confirmChecks** | **Integer** | Matching runs in a row before acting. Defaults to 1. |  [optional] |
|**hold** | [**AdRuleConditions**](AdRuleConditions.md) | Keeps an open alert open after the conditions stop matching. |  [optional] |
|**critical** | [**AdRuleConditions**](AdRuleConditions.md) | Marks an open alert critical. |  [optional] |



