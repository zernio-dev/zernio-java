

# TreasuryTransfer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**payeeId** | **String** | 24-character payee id |  [optional] |
|**payeeName** | **String** | The payee&#39;s name when Zernio knows it, for example a creator&#39;s display name in one of your creator campaigns; null otherwise |  [optional] |
|**destinationType** | [**DestinationTypeEnum**](#DestinationTypeEnum) |  |  [optional] |
|**amountCents** | **Integer** | Amount the payee receives, in full |  [optional] |
|**feeCents** | **Integer** | Zernio fee added on top, 4% with a 50 cent minimum |  [optional] |
|**totalCents** | **Integer** | Amount debited from your balance: amountCents plus feeCents |  [optional] |
|**currency** | **String** |  |  [optional] |
|**reference** | [**TreasuryTransferReference**](TreasuryTransferReference.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**failureReason** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: DestinationTypeEnum

| Name | Value |
|---- | -----|
| CREATOR | &quot;creator&quot; |
| AD_ACCOUNT | &quot;ad_account&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| PAID | &quot;paid&quot; |
| FAILED | &quot;failed&quot; |
| REVERSED | &quot;reversed&quot; |



