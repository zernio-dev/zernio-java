

# CreateSharedBudgetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
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



