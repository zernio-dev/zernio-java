

# CreateSharedBudgetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**accountId** | **String** | Google ads SocialAccount id. |  |
|**adAccountId** | **String** | Platform ad account ID (Google customer ID, digits only). Defaults to the account&#39;s connected customer. |  [optional] |
|**name** | **String** |  |  |
|**amount** | **BigDecimal** | Daily amount in the account&#39;s currency units. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Only daily is accepted (lifetime returns 422). |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| LIFETIME | &quot;lifetime&quot; |



