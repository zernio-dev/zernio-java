

# BusinessAgentBudget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetId** | **String** | Pass it back to edit an existing budget; omit to add one. |  [optional] |
|**unitType** | [**UnitTypeEnum**](#UnitTypeEnum) | Tokens count across the Business Manager, AI turns per conversation. |  |
|**timeWindow** | [**TimeWindowEnum**](#TimeWindowEnum) | Rolling window in the WABA timezone. |  |
|**maxBudget** | **Integer** |  |  |



## Enum: UnitTypeEnum

| Name | Value |
|---- | -----|
| TOKEN | &quot;token&quot; |
| AI_TURN | &quot;ai_turn&quot; |



## Enum: TimeWindowEnum

| Name | Value |
|---- | -----|
| ONE_DAY | &quot;one_day&quot; |
| SEVEN_DAYS | &quot;seven_days&quot; |
| FOURTEEN_DAYS | &quot;fourteen_days&quot; |
| THIRTY_DAYS | &quot;thirty_days&quot; |



