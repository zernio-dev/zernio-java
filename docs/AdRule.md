

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
|**conditions** | [**AdRuleConditions**](AdRuleConditions.md) |  |  |
|**actions** | [**List&lt;AdRuleAction&gt;**](AdRuleAction.md) | Each type at most once, and at most one of &#x60;pause&#x60;, &#x60;activate&#x60; and &#x60;adjust_budget&#x60;. |  |
|**schedule** | [**AdRuleSchedule**](AdRuleSchedule.md) |  |  |
|**cooldownMinutes** | **Integer** |  |  |
|**enabled** | **Boolean** |  |  |
|**lastRunAt** | **OffsetDateTime** |  |  |
|**nextRunAt** | **OffsetDateTime** | Null while the rule is disabled. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |



