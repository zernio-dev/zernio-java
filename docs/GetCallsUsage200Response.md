

# GetCallsUsage200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**since** | **OffsetDateTime** |  |  [optional] |
|**until** | **OffsetDateTime** |  |  [optional] |
|**groupBy** | [**GroupByEnum**](#GroupByEnum) |  |  [optional] |
|**profile** | [**UsageProfileRef**](UsageProfileRef.md) | Present with &#x60;profileId&#x60; / &#x60;externalId&#x60;: the profile the figures are scoped to. |  [optional] |
|**totals** | [**GetCallsUsage200ResponseTotals**](GetCallsUsage200ResponseTotals.md) |  |  [optional] |
|**groups** | [**List&lt;GetCallsUsage200ResponseGroupsInner&gt;**](GetCallsUsage200ResponseGroupsInner.md) | Present (possibly empty) when &#x60;groupBy&#x60; is set. |  [optional] |



## Enum: GroupByEnum

| Name | Value |
|---- | -----|
| DAY | &quot;day&quot; |
| NUMBER | &quot;number&quot; |
| CHANNEL | &quot;channel&quot; |
| PROFILE | &quot;profile&quot; |



