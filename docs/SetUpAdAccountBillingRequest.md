

# SetUpAdAccountBillingRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**accountId** | **String** | Google ads SocialAccount id. |  |
|**adAccountId** | **String** | Google Ads customer id to bill, digits only. |  |
|**paymentsAccountId** | **String** | Monthly invoicing payments account from GET /v1/ads/accounts/billing. |  |
|**spendingLimit** | **BigDecimal** | Account budget cap in the account currency. Omit for an unlimited budget. |  [optional] |
|**budgetName** | **String** |  |  [optional] |
|**purchaseOrderNumber** | **String** | Printed on the invoice. No effect on delivery. |  [optional] |
|**validateOnly** | **Boolean** |  |  [optional] |



