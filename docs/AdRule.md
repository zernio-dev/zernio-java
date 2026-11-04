

# AdRule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**name** | **String** |  |  |
|**accountId** | **String** | The ads connection the rule acts through. |  |
|**platform** | **String** | Ad platform, for example &#x60;facebook&#x60; (Meta) or &#x60;google&#x60;. |  |
|**adAccountId** | **String** | Platform ad account ID. |  |
|**level** | **AdRuleLevel** |  |  |
|**campaignIds** | **List&lt;String&gt;** | Platform campaign IDs the rule is limited to. Null checks the whole ad account. |  |
|**filters** | [**List&lt;AdRuleFiltersInner&gt;**](AdRuleFiltersInner.md) | Narrows the objects the rule checks. Every filter must hold. A campaign rule reads &#x60;name&#x60;, &#x60;campaign_id&#x60;, &#x60;goal&#x60; and &#x60;days_live&#x60;; an ad set rule also &#x60;campaign_name&#x60; and &#x60;adset_id&#x60;; an ad rule also &#x60;adset_name&#x60; and &#x60;ad_id&#x60;. |  |
|**lifecycle** | [**AdRuleLifecycle**](AdRuleLifecycle.md) |  |  |
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  |
|**actions** | [**List&lt;AdRuleAction&gt;**](AdRuleAction.md) | Each type at most once, and at most one of &#x60;pause&#x60;, &#x60;activate&#x60;, &#x60;adjust_budget&#x60;, &#x60;adjust_bid&#x60;, &#x60;duplicate&#x60; and &#x60;edit_name&#x60;. |  |
|**schedule** | [**AdRuleSchedule**](AdRuleSchedule.md) |  |  |
|**cooldownMinutes** | **Integer** |  |  |
|**enabled** | **Boolean** |  |  |
|**lastRunAt** | **OffsetDateTime** |  |  |
|**nextRunAt** | **OffsetDateTime** | Null while the rule is disabled. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |



