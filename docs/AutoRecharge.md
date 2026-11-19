

# AutoRecharge


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether auto top-up is on. Charges happen only when this is true and disabledReason is null. |  |
|**belowCents** | **Integer** | The below amount, in cents: when the balance drops below this, auto top-up brings it back to toCents. |  |
|**toCents** | **Integer** | The back-to amount, in cents. The charge is toCents minus the balance (at least $5, at most toCents unless the balance is below $0 or a monthly fee is due), plus tax. |  |
|**monthlyLimitCents** | **Integer** | Most auto top-up may add per calendar month (UTC), before tax; null for no limit. |  |
|**alertBelowCents** | **Integer** | Low-balance email threshold, sent once per drop below it; null for none. |  |
|**disabledReason** | [**DisabledReasonEnum**](#DisabledReasonEnum) | &#x60;payment_failed&#x60; once a declined charge is not retried, or its one retry fails; updating the card clears it. &#x60;charge_error&#x60; after 24 charges in a row failed for a reason other than a decline; turning auto top-up back on (&#x60;enabled: true&#x60;) clears it. |  |
|**disabledCause** | [**DisabledCauseEnum**](#DisabledCauseEnum) | With &#x60;charge_error&#x60;: &#x60;billing_address&#x60; when the last failure was a billing address that tax cannot be worked out from (fix it, then turn auto top-up back on). Null otherwise. |  |
|**retryCount** | **Integer** | Failed charges in a row; 0 once one goes through. |  |
|**nextRetryAt** | **OffsetDateTime** | When a declined auto top-up is tried again; null when none is waiting. |  |
|**monthRechargedCents** | **Integer** | Auto top-ups this calendar month (UTC), paid or being paid, before tax. |  |



## Enum: DisabledReasonEnum

| Name | Value |
|---- | -----|
| PAYMENT_FAILED | &quot;payment_failed&quot; |
| CHARGE_ERROR | &quot;charge_error&quot; |



## Enum: DisabledCauseEnum

| Name | Value |
|---- | -----|
| BILLING_ADDRESS | &quot;billing_address&quot; |



