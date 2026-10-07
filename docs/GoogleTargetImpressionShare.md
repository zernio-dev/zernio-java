

# GoogleTargetImpressionShare

Google only. Target impression share bidding (Search campaigns only): Google sets bids so the ads show in `location` for `percent` of eligible impressions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | [**LocationEnum**](#LocationEnum) |  |  |
|**percent** | **BigDecimal** | Target share of impressions, in percent (65 &#x3D; 65%). Sent to Google as location_fraction_micros (1% &#x3D; 10,000). |  |
|**maxCpc** | **BigDecimal** | Max CPC bid limit, in the account&#39;s currency units. Google requires it. |  |



## Enum: LocationEnum

| Name | Value |
|---- | -----|
| ANYWHERE_ON_PAGE | &quot;ANYWHERE_ON_PAGE&quot; |
| TOP_OF_PAGE | &quot;TOP_OF_PAGE&quot; |
| ABSOLUTE_TOP_OF_PAGE | &quot;ABSOLUTE_TOP_OF_PAGE&quot; |



