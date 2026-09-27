

# GoogleRecommendation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceName** | **String** | customers/{customerId}/recommendations/{id}. Pass it to apply or dismiss. |  |
|**id** | **String** |  |  |
|**type** | **String** | Google RecommendationType, such as CAMPAIGN_BUDGET, KEYWORD or SET_TARGET_CPA. |  |
|**dismissed** | **Boolean** |  |  |
|**campaignId** | **String** |  |  |
|**campaignIds** | **List&lt;String&gt;** | Every campaign the recommendation targets (several for account-level types). |  |
|**adGroupId** | **String** |  |  |
|**campaignBudgetId** | **String** |  |  |
|**impact** | [**GoogleRecommendationImpact**](GoogleRecommendationImpact.md) |  |  |
|**details** | **Object** | The type-specific recommendation payload exactly as Google returns it (camelCase, amounts in micros), for example recommendedTargetCpaMicros or budgetOptions. |  |



