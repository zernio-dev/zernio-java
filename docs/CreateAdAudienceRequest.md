

# CreateAdAudienceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**adAccountId** | **String** | Must start with act_ |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**pixelId** | **String** | Required for website audiences |  [optional] |
|**retentionDays** | **Integer** | Required for website audiences |  [optional] |
|**sourceAudienceId** | **String** | Required for lookalike audiences |  [optional] |
|**country** | **String** | 2-letter code, required for lookalike audiences |  [optional] |
|**ratio** | **BigDecimal** | Required for lookalike audiences |  [optional] |
|**rule** | **Object** | Pixel event rule for website audiences (optional) |  [optional] |
|**customerFileSource** | **String** | Data source declaration for GDPR compliance (customer_list only) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_LIST | &quot;customer_list&quot; |
| WEBSITE | &quot;website&quot; |
| LOOKALIKE | &quot;lookalike&quot; |



