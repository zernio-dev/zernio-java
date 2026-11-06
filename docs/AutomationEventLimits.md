

# AutomationEventLimits

The limits of an event or scheduled automation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cooldown** | **String** | How long the same post or account is left alone after the automation acts on it, rounded up to whole minutes. None by default. |  [optional] |
|**maxChangesPerDay** | **Integer** | Most runs across the last 24 hours. Required, up to 20, with a boost step. |  [optional] |



