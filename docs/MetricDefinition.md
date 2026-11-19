

# MetricDefinition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**description** | **String** |  |  |
|**unit** | [**UnitEnum**](#UnitEnum) | ratio is a plain ratio (0 to 1 for a rate); money is in the account currency, or the unit and currency meta.units gives; position is a rank where 1 is the top; score runs from 0 to 100. |  |
|**additive** | **Boolean** |  |  |
|**source** | [**SourceEnum**](#SourceEnum) | stored: read from what Zernio synced; live: read from the platform on each request. |  |
|**platforms** | **List&lt;String&gt;** |  |  |
|**freshness** | **String** |  |  |
|**granularities** | [**List&lt;GranularitiesEnum&gt;**](#List&lt;GranularitiesEnum&gt;) |  |  |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;count&quot; |
| MILLISECONDS | &quot;milliseconds&quot; |
| PERCENT | &quot;percent&quot; |
| SECONDS | &quot;seconds&quot; |
| MINUTES | &quot;minutes&quot; |
| RATIO | &quot;ratio&quot; |
| MONEY | &quot;money&quot; |
| POSITION | &quot;position&quot; |
| SCORE | &quot;score&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| STORED | &quot;stored&quot; |
| LIVE | &quot;live&quot; |



## Enum: List&lt;GranularitiesEnum&gt;

| Name | Value |
|---- | -----|
| TOTAL | &quot;total&quot; |
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |



