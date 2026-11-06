

# UpdateAutomationAdAccountControlsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The ads connection that reaches the ad account. |  |
|**adAccountId** | **String** | The platform&#39;s ad account id. |  |
|**paused** | **Boolean** | True stops every automation on this ad account; false lets them run again. |  [optional] |
|**dailyRaiseLimit** | **BigDecimal** | The most automations may raise budgets on this ad account in any 24 hours, in the ad account&#39;s currency. A raise past it is cut to the room left.  Send null to remove the limit.  |  [optional] |



