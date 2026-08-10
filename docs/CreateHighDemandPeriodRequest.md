

# CreateHighDemandPeriodRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id used to resolve the Meta token. |  |
|**campaignId** | **String** | Platform campaign id. Exactly one of campaignId / adSetId. |  [optional] |
|**adSetId** | **String** | Platform ad set id. Exactly one of campaignId / adSetId. |  [optional] |
|**budgetValue** | **BigDecimal** | With ABSOLUTE, a budget in the ad account&#39;s currency in WHOLE units (50 &#x3D; $50.00). With MULTIPLIER, a factor of the existing budget (2 &#x3D; double it) and NOT a currency amount. |  |
|**budgetValueType** | [**BudgetValueTypeEnum**](#BudgetValueTypeEnum) |  |  |
|**timeStart** | **Integer** | Unix seconds, on a 15-minute boundary (:00, :15, :30, :45). |  |
|**timeEnd** | **Integer** | Unix seconds, on a 15-minute boundary and after timeStart. |  |
|**recurrenceType** | [**RecurrenceTypeEnum**](#RecurrenceTypeEnum) |  |  [optional] |
|**currency** | **String** | Ad account currency, for the ABSOLUTE minor-unit conversion. Ignored for MULTIPLIER. |  [optional] |



## Enum: BudgetValueTypeEnum

| Name | Value |
|---- | -----|
| ABSOLUTE | &quot;ABSOLUTE&quot; |
| MULTIPLIER | &quot;MULTIPLIER&quot; |



## Enum: RecurrenceTypeEnum

| Name | Value |
|---- | -----|
| ONE_TIME | &quot;ONE_TIME&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |



