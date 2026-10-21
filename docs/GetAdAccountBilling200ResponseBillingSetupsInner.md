

# GetAdAccountBilling200ResponseBillingSetupsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingSetupId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | APPROVED_HELD means approved but waiting for its first account budget to be approved. |  [optional] |
|**paymentsAccountId** | **String** |  |  [optional] |
|**startDateTime** | **String** | In the account time zone, as Google returns it. |  [optional] |
|**endDateTime** | **String** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| APPROVED_HELD | &quot;APPROVED_HELD&quot; |
| APPROVED | &quot;APPROVED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



