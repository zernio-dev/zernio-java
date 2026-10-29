

# AdRuleRunEvaluationNotification

Set when a run of a rule with a `notify` action matched objects and tried to send the webhook. A notify-only rule whose webhook fails ends with outcome `failed`.  - `done`: the `ad_rule.triggered` webhook is queued for the webhooks subscribed to it (with none subscribed it is still `done`, but nothing is delivered). - `failed`: it could not be queued. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**reason** | **String** | Why the webhook could not be queued. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DONE | &quot;done&quot; |
| FAILED | &quot;failed&quot; |



