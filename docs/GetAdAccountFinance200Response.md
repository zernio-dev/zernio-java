

# GetAdAccountFinance200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** |  |  [optional] |
|**currency** | **String** | ISO 4217 code all money values are expressed in. |  [optional] |
|**balance** | **BigDecimal** | Outstanding/prepaid balance in whole currency units. |  [optional] |
|**amountSpent** | **BigDecimal** | Lifetime amount spent in whole currency units. |  [optional] |
|**spendCap** | **BigDecimal** | Account spend cap; null when none is set. |  [optional] |
|**fundingSource** | [**GetAdAccountFinance200ResponseFundingSource**](GetAdAccountFinance200ResponseFundingSource.md) |  |  [optional] |



