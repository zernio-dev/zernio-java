

# AutomationStepOneOf9

Moves daily budget from the matched objects ranked worst by `metric` over `window` to those ranked best. The total stays the same.  Send `by` (a percent of each giver's budget) or `amount` (in all, split evenly), not both. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**metric** | **String** | A condition metric or &#x60;result:&lt;key&gt;&#x60;, not a calendar metric. |  |
|**window** | **String** | A condition window. |  |
|**best** | [**BestEnum**](#BestEnum) | Which end is best. Defaults to lowest for &#x60;cpa&#x60;, &#x60;cpc&#x60;, &#x60;cpm&#x60;, &#x60;frequency&#x60; and cost results, highest otherwise. |  [optional] |
|**from** | **Integer** | How many objects give budget. |  |
|**to** | **Integer** | How many objects receive it. |  |
|**by** | **String** | From 1% to 90%. |  [optional] |
|**amount** | **BigDecimal** |  |  [optional] |
|**min** | **BigDecimal** | A giver&#39;s budget never goes below this. |  [optional] |
|**max** | **BigDecimal** | A receiver&#39;s budget never goes above this. |  [optional] |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| REALLOCATE | &quot;reallocate&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADS_REALLOCATE_BUDGET | &quot;ads.reallocate_budget&quot; |



## Enum: BestEnum

| Name | Value |
|---- | -----|
| HIGHEST | &quot;highest&quot; |
| LOWEST | &quot;lowest&quot; |



