

# UpdateAdSet200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budget** | [**AdBudget**](AdBudget.md) |  |  [optional] |
|**budgetLevel** | [**BudgetLevelEnum**](#BudgetLevelEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status written to the ad set switch |  [optional] |
|**statusUpdated** | **Integer** | Number of ads whose own stored status changed alongside the ad set switch |  [optional] |
|**statusSkipped** | **Integer** | Number of ads whose own status was left as it was |  [optional] |
|**statusSkippedReasons** | **List&lt;String&gt;** | Why each group of ads was skipped |  [optional] |
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



