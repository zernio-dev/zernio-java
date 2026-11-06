

# AutomationNotifyStep

Sends a summary to Slack channels or email addresses of connected accounts. In an ad rule it also sends the `ad_rule.triggered` webhook, and `to` is optional.  Event and scheduled automations need `to`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | In an ad rule the id is always &#x60;notify&#x60;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**to** | [**List&lt;AutomationNotifyStepToInner&gt;**](AutomationNotifyStepToInner.md) | Up to 5 in an ad rule. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NOTIFY_SEND | &quot;notify.send&quot; |



