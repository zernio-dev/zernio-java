

# CPM


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**metric** | [**MetricEnum**](#MetricEnum) | What the rate pays on. Missing means views. |  [optional] |
|**engagementTypes** | [**List&lt;EngagementTypesEnum&gt;**](#List&lt;EngagementTypesEnum&gt;) | The engagements that count. Missing means all four. |  [optional] |
|**organicViewsOnly** | **Boolean** | Only organic views count; views from ads do not. |  [optional] |
|**ratePer1kCents** | **Integer** |  |  |
|**minViewsToEarn** | **Integer** |  |  |
|**maxPayoutPerClipCents** | **Integer** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CPM | &quot;cpm&quot; |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| VIEWS | &quot;views&quot; |
| ENGAGEMENTS | &quot;engagements&quot; |



## Enum: List&lt;EngagementTypesEnum&gt;

| Name | Value |
|---- | -----|
| LIKES | &quot;likes&quot; |
| COMMENTS | &quot;comments&quot; |
| SHARES | &quot;shares&quot; |
| SAVES | &quot;saves&quot; |



