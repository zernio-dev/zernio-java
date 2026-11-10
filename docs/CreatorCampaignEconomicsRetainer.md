

# CreatorCampaignEconomicsRetainer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**mode** | [**ModeEnum**](#ModeEnum) | &#x60;standard&#x60; pays &#x60;amountCents&#x60; per period. &#x60;smart&#x60; guarantees it: the commission the creator earned in the period is topped up to &#x60;amountCents&#x60;. Smart needs &#x60;commission&#x60; and a linked store. |  [optional] |
|**amountCents** | **Integer** |  |  |
|**period** | [**PeriodEnum**](#PeriodEnum) | Weeks start Monday 00:00 UTC, months on the 1st. A period is paid within a day after it ends. A standard &#x60;once&#x60; retainer pays as soon as the posts are approved; a smart one when the campaign ends. |  |
|**requiredApprovedPosts** | **Integer** | Posts approved within the period that it needs. 0 pays without posts. |  |
|**commission** | [**CreatorCampaignCommissionTerms**](CreatorCampaignCommissionTerms.md) |  |  [optional] |
|**budgetCents** | **Integer** |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RETAINER | &quot;retainer&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;standard&quot; |
| SMART | &quot;smart&quot; |



## Enum: PeriodEnum

| Name | Value |
|---- | -----|
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |
| ONCE | &quot;once&quot; |



