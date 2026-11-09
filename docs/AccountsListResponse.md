

# AccountsListResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accounts** | [**List&lt;ListedAccount&gt;**](ListedAccount.md) |  |  |
|**hasAnalyticsAccess** | **Boolean** | Whether user has analytics add-on access |  |
|**pagination** | [**AccountsListResponsePagination**](AccountsListResponsePagination.md) |  |  [optional] |
|**warning** | **String** | Only when an unpaged API request was cut at 500 accounts: how to list the rest with cursor paging. |  [optional] |
|**profileTotals** | **Map&lt;String, Integer&gt;** | Only with profileIds and perProfile. Accounts matching the filters per profile ID; a profile with none is absent. |  [optional] |
|**statusCounts** | [**AccountsListResponseStatusCounts**](AccountsListResponseStatusCounts.md) |  |  [optional] |



