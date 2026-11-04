

# CreateAdRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**accountId** | **String** | The ads connection (account ID from &#x60;GET /v1/accounts&#x60;). |  |
|**adAccountId** | **String** | Platform ad account ID, from &#x60;GET /v1/ads/accounts&#x60;. |  |
|**level** | **AdRuleLevel** |  |  |
|**campaignIds** | **List&lt;String&gt;** | Only check these platform campaign IDs (or their ad sets). Leave out to check the whole ad account. |  [optional] |
|**filters** | [**List&lt;AdRuleFiltersInner&gt;**](AdRuleFiltersInner.md) | Narrows the objects the rule checks. Every filter must hold. A campaign rule reads &#x60;name&#x60;, &#x60;campaign_id&#x60;, &#x60;goal&#x60; and &#x60;days_live&#x60;; an ad set rule also &#x60;campaign_name&#x60; and &#x60;adset_id&#x60;; an ad rule also &#x60;adset_name&#x60; and &#x60;ad_id&#x60;. |  [optional] |
|**lifecycle** | [**AdRuleLifecycle**](AdRuleLifecycle.md) |  |  [optional] |
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  |
|**actions** | [**List&lt;AdRuleAction&gt;**](AdRuleAction.md) | Each type at most once, and at most one of &#x60;pause&#x60;, &#x60;activate&#x60;, &#x60;adjust_budget&#x60;, &#x60;adjust_bid&#x60;, &#x60;duplicate&#x60; and &#x60;edit_name&#x60;. |  |
|**schedule** | [**AdRuleSchedule**](AdRuleSchedule.md) | Leave it out to run every 60 minutes. |  [optional] |
|**cooldownMinutes** | **Integer** | How long the rule leaves an object alone after acting on it. |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |



