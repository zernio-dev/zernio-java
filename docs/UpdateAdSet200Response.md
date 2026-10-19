

# UpdateAdSet200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budget** | [**AdBudget**](AdBudget.md) |  |  [optional] |
|**budgetLevel** | [**BudgetLevelEnum**](#BudgetLevelEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | As in PUT /v1/ads/ad-sets/{adSetId}/status: delivery derived from the switches read back. |  [optional] |
|**platformAdSetStatus** | **String** | The ad set&#39;s status read back from the platform, as in PUT /v1/ads/ad-sets/{adSetId}/status (Meta and Reddit return the ad set&#39;s effective_status); null when it could not be read. |  [optional] |
|**platformCampaignStatus** | **String** |  |  [optional] |
|**statusReadAt** | **OffsetDateTime** |  |  [optional] |
|**statusUpdated** | [**StatusUpdatedEnum**](#StatusUpdatedEnum) | 1 when the ad set&#39;s switch was written. |  [optional] |
|**statusSkipped** | [**StatusSkippedEnum**](#StatusSkippedEnum) | 1 when a live read showed it already in the requested state. |  [optional] |
|**statusSkippedReasons** | **List&lt;String&gt;** |  |  [optional] |
|**bidStrategy** | **BidStrategy** |  |  [optional] |
|**bidAmount** | **BigDecimal** |  |  [optional] |
|**roasAverageFloor** | **BigDecimal** |  |  [optional] |
|**platformSpecificData** | **Object** |  |  [optional] |
|**targeting** | **Object** | Present when &#x60;placements&#x60; or &#x60;targeting&#x60; was sent. The ad set&#39;s full Meta targeting as written (Meta snake_case). The same snake_case object is stored as the ad set&#39;s and its ads&#39; &#x60;targeting&#x60;. |  [optional] |



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



