

# AutomationSubjects

What an ad rule checks, and where.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**each** | [**EachEnum**](#EachEnum) | The objects judged one by one. |  |
|**adAccounts** | [**List&lt;AutomationSubjectsAdAccountsInner&gt;**](AutomationSubjectsAdAccountsInner.md) | The ad account to check. One per ad rule, and an edit cannot move it to another. |  |
|**campaignIds** | **List&lt;String&gt;** | Only these platform campaigns or their ad sets and ads. Leave out to check the whole ad account. |  [optional] |
|**filters** | [**List&lt;AutomationAdFilter&gt;**](AutomationAdFilter.md) | All must hold. |  [optional] |
|**groups** | [**List&lt;AutomationSubjectsGroupsInner&gt;**](AutomationSubjectsGroupsInner.md) | Judges campaigns together (campaign rules only): each group&#39;s numbers are summed and its rates computed on the totals, and a matching group acts on each of its campaigns.  A group with no filters holds every campaign the rule checks. &#x60;reach&#x60; and &#x60;frequency&#x60; cannot be used with groups.  |  [optional] |



## Enum: EachEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| ADSET | &quot;adset&quot; |
| AD | &quot;ad&quot; |



