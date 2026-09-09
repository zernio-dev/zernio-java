

# MetaPromotion

Meta explicit Promotion offer. Maps to creative_sourcing_spec.promotion_metadata_spec with promotion_source ADVERTISER_INPUT. Dates become Unix seconds. Send null to omit an explicit offer on a new creative or remove it when rebuilding. Creation success alone does not confirm application: inspect promotionStatus in the response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Promotion type accepted by Meta. PERCENTAGE_OFF values cannot exceed 100. |  |
|**value** | **BigDecimal** | Nonnegative promotion value passed to Meta unchanged. AMOUNT_OFF units are not confirmed, including major versus minor currency units. For PERCENTAGE_OFF this is the percentage discount, at most 100. |  |
|**code** | **String** | Optional promotion code. |  [optional] |
|**startDate** | **OffsetDateTime** | Optional ISO 8601 start timestamp with a timezone offset or Z. |  [optional] |
|**endDate** | **OffsetDateTime** | Optional ISO 8601 end timestamp with a timezone offset or Z. Must be after startDate when both are set. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AMOUNT_OFF | &quot;AMOUNT_OFF&quot; |
| FREE_RETURN | &quot;FREE_RETURN&quot; |
| FREE_SHIPPING | &quot;FREE_SHIPPING&quot; |
| PERCENTAGE_OFF | &quot;PERCENTAGE_OFF&quot; |
| PROMO_CODE | &quot;PROMO_CODE&quot; |



