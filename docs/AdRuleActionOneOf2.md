

# AdRuleActionOneOf2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Reactivate a campaign, ad set or ad a rule paused, once &#x60;cooldownMinutes&#x60; has passed since the pause. Objects you paused yourself are never touched. |  |
|**maxChangesPerDay** | **Integer** | At most this many objects changed in any 24 hours, across runs. Matches over the limit are skipped with &#x60;daily_limit_reached&#x60; and tried again later. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACTIVATE | &quot;activate&quot; |



