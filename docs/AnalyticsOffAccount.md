

# AnalyticsOffAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | - X_ANALYTICS_NOT_ENABLED: &#x60;xCapabilities.analytics&#x60; is off on the account. It is opt-in on usage-based billing. Turn it on with &#x60;PUT /v1/accounts/{accountId}&#x60;, or in the account&#39;s X settings in the dashboard. - X_ANALYTICS_PAUSED: it was on, and the monthly X spend cap turned it off. - PAYMENT_REQUIRED: X access is paused because billing on this account failed.  New values may be added.  |  |
|**message** | **String** | The reason in words. X_ANALYTICS_NOT_ENABLED also says how to turn it on. |  |
|**accountId** | **String** |  |  |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| X_ANALYTICS_NOT_ENABLED | &quot;X_ANALYTICS_NOT_ENABLED&quot; |
| X_ANALYTICS_PAUSED | &quot;X_ANALYTICS_PAUSED&quot; |
| PAYMENT_REQUIRED | &quot;PAYMENT_REQUIRED&quot; |



