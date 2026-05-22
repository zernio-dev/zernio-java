

# UploadedOrDerivedAudience

customer_list, website, or lookalike audience (uploaded or derived from a source).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**adAccountId** | **String** | Platform ad account ID. Must start with act_ for Meta; bare platform id for others (Google customer id, X/TikTok/LinkedIn/Pinterest account id). |  |
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



