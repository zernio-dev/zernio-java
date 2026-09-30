

# GetWhatsAppPricingAnalytics200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**phoneNumber** | **String** | The number the data is scoped to, digits only. |  |
|**granularity** | [**GranularityEnum**](#GranularityEnum) |  |  |
|**start** | **OffsetDateTime** |  |  |
|**end** | **OffsetDateTime** |  |  |
|**dataPoints** | [**List&lt;GetWhatsAppPricingAnalytics200ResponseDataPointsInner&gt;**](GetWhatsAppPricingAnalytics200ResponseDataPointsInner.md) |  |  |



## Enum: GranularityEnum

| Name | Value |
|---- | -----|
| HALF_HOUR | &quot;HALF_HOUR&quot; |
| DAILY | &quot;DAILY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |



