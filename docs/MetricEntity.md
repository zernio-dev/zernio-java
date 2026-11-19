

# MetricEntity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entity** | [**EntityEnum**](#EntityEnum) |  |  |
|**path** | **String** |  |  |
|**requiredScope** | **List&lt;String&gt;** |  |  |
|**maxScopeIds** | **Map&lt;String, Integer&gt;** |  |  |
|**maxRangeDays** | **Integer** |  |  |
|**defaultRangeDays** | **Integer** |  |  |
|**granularities** | [**List&lt;GranularitiesEnum&gt;**](#List&lt;GranularitiesEnum&gt;) |  |  |
|**sorts** | **List&lt;String&gt;** |  |  |
|**maxSortedRows** | **Integer** |  |  |
|**includes** | [**List&lt;MetricEntityIncludesInner&gt;**](MetricEntityIncludesInner.md) |  |  |
|**groupBy** | [**List&lt;MetricEntityGroupByInner&gt;**](MetricEntityGroupByInner.md) |  |  |
|**attributions** | [**List&lt;MetricEntityAttributionsInner&gt;**](MetricEntityAttributionsInner.md) |  |  |
|**origins** | **List&lt;String&gt;** |  |  |
|**metrics** | [**List&lt;MetricDefinition&gt;**](MetricDefinition.md) |  |  |



## Enum: EntityEnum

| Name | Value |
|---- | -----|
| POSTS | &quot;posts&quot; |
| ACCOUNTS | &quot;accounts&quot; |
| INBOX | &quot;inbox&quot; |
| INSIGHTS | &quot;insights&quot; |
| ADS | &quot;ads&quot; |
| CAMPAIGNS | &quot;campaigns&quot; |
| AD_ACCOUNTS | &quot;ad-accounts&quot; |



## Enum: List&lt;GranularitiesEnum&gt;

| Name | Value |
|---- | -----|
| TOTAL | &quot;total&quot; |
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |



