

# CreatorCampaignEconomicsCpm


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**metric** | [**MetricEnum**](#MetricEnum) | What the rate pays on. &#x60;engagements&#x60; counts the &#x60;engagementTypes&#x60; as each platform reports them, and &#x60;minViewsToEarn&#x60; then applies to engagements. Fixed once the campaign leaves draft. |  [optional] |
|**engagementTypes** | [**List&lt;EngagementTypesEnum&gt;**](#List&lt;EngagementTypesEnum&gt;) | With &#x60;metric: engagements&#x60;, the engagements that count. Missing means all four, and sending it on a views campaign answers 400. YouTube reports likes and comments only, Facebook and Threads have no saves, and Pinterest reports saves only. |  [optional] |
|**ratePer1kCents** | **Integer** |  |  |
|**minViewsToEarn** | **Integer** | The count a post must reach before it earns, in the campaign metric (views or engagements). |  |
|**maxPayoutPerClipCents** | **Integer** |  |  [optional] |
|**budgetCents** | **Integer** |  |  |



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



