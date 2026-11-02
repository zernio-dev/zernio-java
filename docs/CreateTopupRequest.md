

# CreateTopupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountCents** | **Integer** | Amount to credit to your balance, in cents: $10 to $100,000. The card fee is charged on top. |  |
|**method** | [**MethodEnum**](#MethodEnum) | Only card is available. bank_transfer returns 400 \&quot;Bank transfers are not available yet.\&quot; |  |
|**paymentMethodId** | **String** | A saved card of the billing owner&#39;s (&#x60;pm_...&#x60;). Defaults to the default payment method. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| CARD | &quot;card&quot; |
| BANK_TRANSFER | &quot;bank_transfer&quot; |



