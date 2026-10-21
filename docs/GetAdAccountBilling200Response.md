

# GetAdAccountBilling200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **String** |  |  [optional] |
|**paymentsAccounts** | [**List&lt;GetAdAccountBilling200ResponsePaymentsAccountsInner&gt;**](GetAdAccountBilling200ResponsePaymentsAccountsInner.md) |  |  [optional] |
|**billingSetups** | [**List&lt;GetAdAccountBilling200ResponseBillingSetupsInner&gt;**](GetAdAccountBilling200ResponseBillingSetupsInner.md) |  |  [optional] |
|**accountBudgets** | [**List&lt;GetAdAccountBilling200ResponseAccountBudgetsInner&gt;**](GetAdAccountBilling200ResponseAccountBudgetsInner.md) |  |  [optional] |
|**pendingBudgetProposals** | [**List&lt;GetAdAccountBilling200ResponsePendingBudgetProposalsInner&gt;**](GetAdAccountBilling200ResponsePendingBudgetProposalsInner.md) | New account budgets proposed but not yet approved by Google. A setup with one is not reused by the POST. |  [optional] |
|**cachedAt** | **OffsetDateTime** | When this data was fetched from Google. Null when the cache is unavailable. |  [optional] |
|**stale** | **Boolean** | True when Google&#39;s quota was exhausted and this is the last successful fetch. |  [optional] |



