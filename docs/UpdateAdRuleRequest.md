

# UpdateAdRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**level** | **AdRuleLevel** |  |  [optional] |
|**campaignIds** | **List&lt;String&gt;** |  |  [optional] |
|**filters** | [**List&lt;AdRuleFiltersInner&gt;**](AdRuleFiltersInner.md) | Narrows the objects the rule checks. Every filter must hold. A campaign rule reads &#x60;name&#x60;, &#x60;campaign_id&#x60;, &#x60;goal&#x60;, &#x60;days_live&#x60; and &#x60;budget_level&#x60;; an ad set rule also &#x60;campaign_name&#x60; and &#x60;adset_id&#x60;; an ad rule also &#x60;adset_name&#x60; and &#x60;ad_id&#x60;. |  [optional] |
|**groups** | [**List&lt;AdRuleGroupsInner&gt;**](AdRuleGroupsInner.md) | Null removes the groups; each campaign is then judged on its own. |  [optional] |
|**lifecycle** | [**AdRuleLifecycle**](AdRuleLifecycle.md) |  |  [optional] |
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  [optional] |
|**actions** | [**List&lt;AdRuleAction&gt;**](AdRuleAction.md) | Each type at most once, and at most one of &#x60;pause&#x60;, &#x60;activate&#x60;, &#x60;adjust_budget&#x60;, &#x60;adjust_bid&#x60;, &#x60;adjust_target&#x60;, &#x60;reallocate_budget&#x60;, &#x60;duplicate&#x60; and &#x60;edit_name&#x60;. |  [optional] |
|**schedule** | [**AdRuleSchedule**](AdRuleSchedule.md) |  |  [optional] |
|**cooldownMinutes** | **Integer** |  |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |



