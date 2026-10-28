

# CreateTopupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountCents** | **Integer** | Amount in cents, minimum $10 |  |
|**method** | [**MethodEnum**](#MethodEnum) | Only card is available. bank_transfer returns 400 \&quot;Bank transfers are not available yet.\&quot; |  |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| CARD | &quot;card&quot; |
| BANK_TRANSFER | &quot;bank_transfer&quot; |



