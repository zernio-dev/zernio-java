

# AccountsListResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accounts** | [**List&lt;SocialAccount&gt;**](SocialAccount.md) |  |  |
|**hasAnalyticsAccess** | **Boolean** | Whether user has analytics add-on access |  |
|**pagination** | [**Pagination**](Pagination.md) | Only present when page/limit params are provided |  [optional] |
|**profileTotals** | **Map&lt;String, Integer&gt;** | Only with profileIds and perProfile. Accounts matching the filters per profile ID; a profile with none is absent. |  [optional] |
|**statusCounts** | [**AccountsListResponseStatusCounts**](AccountsListResponseStatusCounts.md) |  |  [optional] |



