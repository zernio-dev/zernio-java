

# AutomationLimits

An ad rule's limits.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cooldown** | **String** | How long an object is left alone after the rule acts on it. Whole minutes, up to &#x60;30d&#x60;. |  [optional] |
|**maxChangesPerDay** | **Integer** | Most changes across the last 24 hours. Needs an &#x60;ads.*&#x60; step. |  [optional] |
|**maxChangesPerObject** | **Integer** | Most times the rule may change one object, over its whole history. Needs an &#x60;ads.*&#x60; step. |  [optional] |



