

# GetSmsUsage200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**since** | **OffsetDateTime** |  |  [optional] |
|**until** | **OffsetDateTime** |  |  [optional] |
|**groupBy** | [**GroupByEnum**](#GroupByEnum) |  |  [optional] |
|**profile** | [**UsageProfileRef**](UsageProfileRef.md) | Present with &#x60;profileId&#x60; / &#x60;externalId&#x60;: the profile the counts are scoped to. |  [optional] |
|**totals** | [**GetSmsUsage200ResponseTotals**](GetSmsUsage200ResponseTotals.md) |  |  [optional] |
|**groups** | [**List&lt;GetSmsUsage200ResponseGroupsInner&gt;**](GetSmsUsage200ResponseGroupsInner.md) | Present (possibly empty) when &#x60;groupBy&#x60; is set. |  [optional] |



## Enum: GroupByEnum

| Name | Value |
|---- | -----|
| DAY | &quot;day&quot; |
| NUMBER | &quot;number&quot; |
| PROFILE | &quot;profile&quot; |



