

# AutomationTemplateInput

Something an install asks for. Each automation in the template holds `{ \"$input\": \"<key>\" }` where the value goes, and installing puts the value sent in `inputs.<key>` there.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The name to send the value under in &#x60;inputs&#x60;, for example &#x60;adAccount&#x60;. |  |
|**type** | [**TypeEnum**](#TypeEnum) | What the value is. &#x60;ad_account&#x60;: &#x60;{ accountId, adAccountId }&#x60;. &#x60;profile&#x60;: a profile id. &#x60;social_accounts&#x60;: an array of social account ids. &#x60;notify_destination&#x60;: an array of &#x60;{ accountId, to?, channelId? }&#x60;. &#x60;number&#x60;, &#x60;money&#x60; (in the ad account&#39;s currency) and &#x60;percent&#x60;: a number within the bounds below. &#x60;choice&#x60;: one of &#x60;options[].value&#x60;. |  |
|**label** | **String** |  |  |
|**optional** | **Boolean** | True when an install may leave it out. A field that points at a left-out input is dropped. |  [optional] |
|**_default** | [**AutomationTemplateInputDefault**](AutomationTemplateInputDefault.md) |  |  [optional] |
|**min** | **BigDecimal** |  |  [optional] |
|**exclusiveMin** | **BigDecimal** | The value must be above it, for example an amount above 0. |  [optional] |
|**max** | **BigDecimal** |  |  [optional] |
|**integer** | **Boolean** | True when only whole numbers are accepted. |  [optional] |
|**options** | [**List&lt;AutomationTemplateInputOptionsInner&gt;**](AutomationTemplateInputOptionsInner.md) | What a &#x60;choice&#x60; input offers. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AD_ACCOUNT | &quot;ad_account&quot; |
| PROFILE | &quot;profile&quot; |
| SOCIAL_ACCOUNTS | &quot;social_accounts&quot; |
| NOTIFY_DESTINATION | &quot;notify_destination&quot; |
| NUMBER | &quot;number&quot; |
| MONEY | &quot;money&quot; |
| PERCENT | &quot;percent&quot; |
| CHOICE | &quot;choice&quot; |



