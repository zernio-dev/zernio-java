

# UpdateAdSet200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budget** | [**AdBudget**](AdBudget.md) |  |  [optional] |
|**budgetLevel** | [**BudgetLevelEnum**](#BudgetLevelEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | As in PUT /v1/ads/ad-sets/{adSetId}/status: delivery derived from the switches read back. |  [optional] |
|**platformAdSetStatus** | **String** | The ad set&#39;s own switch read back from the platform; null when it could not be read. |  [optional] |
|**platformCampaignStatus** | **String** |  |  [optional] |
|**statusReadAt** | **OffsetDateTime** |  |  [optional] |
|**statusUpdated** | [**StatusUpdatedEnum**](#StatusUpdatedEnum) | 1 when the ad set&#39;s switch was written. |  [optional] |
|**statusSkipped** | [**StatusSkippedEnum**](#StatusSkippedEnum) | 1 when a live read showed it already in the requested state. |  [optional] |
|**statusSkippedReasons** | **List&lt;String&gt;** |  |  [optional] |
|**bidStrategy** | **BidStrategy** |  |  [optional] |
|**bidAmount** | **BigDecimal** |  |  [optional] |
|**roasAverageFloor** | **BigDecimal** |  |  [optional] |
|**platformSpecificData** | **Object** |  |  [optional] |



## Enum: BudgetLevelEnum

| Name | Value |
|---- | -----|
| ADSET | &quot;adset&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



## Enum: StatusUpdatedEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



## Enum: StatusSkippedEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



