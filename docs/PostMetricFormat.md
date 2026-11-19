

# PostMetricFormat


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**format** | [**FormatEnum**](#FormatEnum) | gif counts as image, document as text. |  |
|**postCount** | **Integer** | Posts of the format published in the range. |  |
|**metrics** | **Map&lt;String, BigDecimal&gt;** | Each metric asked, summed over the newest posts of the range up to meta.metricsSample.limit; engagementRate pools them. |  |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| CAROUSEL | &quot;carousel&quot; |
| TEXT | &quot;text&quot; |



