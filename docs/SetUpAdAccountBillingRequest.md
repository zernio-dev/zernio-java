

# SetUpAdAccountBillingRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Google ads SocialAccount id. |  |
|**adAccountId** | **String** | Google Ads customer id to bill, digits only. |  |
|**paymentsAccountId** | **String** | Monthly invoicing payments account from GET /v1/ads/accounts/billing. |  |
|**spendingLimit** | **BigDecimal** | Account budget cap in the account currency. Omit for an unlimited budget. |  [optional] |
|**budgetName** | **String** |  |  [optional] |
|**purchaseOrderNumber** | **String** | Printed on the invoice. No effect on delivery. |  [optional] |
|**validateOnly** | **Boolean** |  |  [optional] |



