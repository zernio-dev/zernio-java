

# AutoRecharge


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether auto top-up is on. Charges happen only when this is true and disabledReason is null. |  |
|**belowCents** | **Integer** | Auto top-up charges the card when the balance drops below this, in cents. |  |
|**toCents** | **Integer** | Top back up to this, in cents. The charge is toCents minus the balance, plus tax. |  |
|**monthlyLimitCents** | **Integer** | Most auto top-up may add per calendar month (UTC), before tax; null for no limit. |  |
|**alertBelowCents** | **Integer** | Low-balance email threshold, sent once per drop below it; null for none. |  |
|**disabledReason** | [**DisabledReasonEnum**](#DisabledReasonEnum) | &#x60;payment_failed&#x60; after four failed charges in a row. Updating the card clears it. |  |
|**retryCount** | **Integer** | Failed charges in a row; 0 once one goes through. |  |
|**nextRetryAt** | **OffsetDateTime** | When a declined auto top-up is tried again; null when none is waiting. |  |
|**monthRechargedCents** | **Integer** | Auto top-ups this calendar month (UTC), paid or being paid, before tax. |  |



## Enum: DisabledReasonEnum

| Name | Value |
|---- | -----|
| PAYMENT_FAILED | &quot;payment_failed&quot; |



