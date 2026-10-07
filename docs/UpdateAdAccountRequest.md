

# UpdateAdAccountRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID (metaads, or a facebook/instagram posting account) |  |
|**adAccountId** | **String** | Meta ad account ID (act_...) |  |
|**name** | **String** | New ad account name. |  [optional] |
|**spendCap** | **BigDecimal** | Account spend cap in whole currency units; null removes it. |  [optional] |
|**resetAmountSpent** | **Boolean** | Restart the amount counted against the cap from zero. Cannot be combined with spendCap null. |  [optional] |
|**defaultDsaBeneficiary** | **String** | Legal entity benefiting from ads on this ad account |  [optional] |
|**defaultDsaPayor** | **String** | Legal entity paying for ads on this ad account. Defaults to defaultDsaBeneficiary when omitted. Requires defaultDsaBeneficiary. |  [optional] |
|**trackingUrlTemplate** | **String** | **Google only.** Account tracking template (customer.tracking_url_template); an empty string clears it. |  [optional] |
|**finalUrlSuffix** | **String** | **Google only.** Account final URL suffix (customer.final_url_suffix); an empty string clears it. |  [optional] |



