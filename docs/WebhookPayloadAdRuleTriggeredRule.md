

# WebhookPayloadAdRuleTriggeredRule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Zernio ad rule ID. |  |
|**name** | **String** |  |  |
|**level** | [**LevelEnum**](#LevelEnum) | Whether the rule evaluates campaigns, ad sets, ads, Google keywords or Google search terms. |  |
|**platformAdAccountId** | **String** | Platform-native ad account ID the rule watches. |  |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| ADSET | &quot;adset&quot; |
| AD | &quot;ad&quot; |
| KEYWORD | &quot;keyword&quot; |
| SEARCH_TERM | &quot;search_term&quot; |



