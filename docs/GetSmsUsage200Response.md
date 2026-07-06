

# GetSmsUsage200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**since** | **OffsetDateTime** |  |  [optional] |
|**until** | **OffsetDateTime** |  |  [optional] |
|**groupBy** | [**GroupByEnum**](#GroupByEnum) |  |  [optional] |
|**totals** | [**GetSmsUsage200ResponseTotals**](GetSmsUsage200ResponseTotals.md) |  |  [optional] |
|**groups** | [**List&lt;GetSmsUsage200ResponseGroupsInner&gt;**](GetSmsUsage200ResponseGroupsInner.md) | Present (possibly empty) when &#x60;groupBy&#x60; is set. |  [optional] |



## Enum: GroupByEnum

| Name | Value |
|---- | -----|
| DAY | &quot;day&quot; |
| NUMBER | &quot;number&quot; |



