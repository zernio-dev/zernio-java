

# AutomationAlert

Turns matches into alerts: the ad rule acts only after `confirmChecks` matching checks in a row, keeps the alert open while `hold` holds and marks it critical when `critical` holds.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confirmChecks** | **Integer** |  |  [optional] |
|**hold** | [**AdRuleConditions**](AdRuleConditions.md) |  |  [optional] |
|**critical** | [**AdRuleConditions**](AdRuleConditions.md) |  |  [optional] |



