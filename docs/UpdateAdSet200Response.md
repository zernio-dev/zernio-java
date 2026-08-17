

# UpdateAdSet200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budget** | [**AdBudget**](AdBudget.md) |  |  [optional] |
|**budgetLevel** | [**BudgetLevelEnum**](#BudgetLevelEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status written to the ad set. Absent when nothing was written (see statusMessage). |  [optional] |
|**statusUpdated** | **Integer** | Number of ads whose own stored status changed alongside the ad set switch |  [optional] |
|**statusSkipped** | **Integer** | Number of ads whose own status was left as it was |  [optional] |
|**statusSkippedReasons** | **List&lt;String&gt;** | Why each group of ads was skipped |  [optional] |
|**statusMessage** | **String** | Present only where the platform has no ad-set switch and no child ad was actionable; &#x60;status&#x60; is then absent because nothing was written |  [optional] |
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



