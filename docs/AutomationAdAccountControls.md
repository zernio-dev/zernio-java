

# AutomationAdAccountControls


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The connection your automations reach the ad account through; null when no automation uses it any more. |  |
|**platform** | **String** | The ad platform, for example &#x60;facebook&#x60;. |  |
|**adAccountId** | **String** | The platform&#39;s ad account id. |  |
|**paused** | **Boolean** | True when every ad rule on this ad account is stopped. |  |
|**pausedAt** | **OffsetDateTime** |  |  |
|**dailyRaiseLimit** | **BigDecimal** | The most automations may raise budgets on this ad account in any 24 hours, in the ad account&#39;s currency. Null when there is no limit. |  |



