

# CampaignLedgerEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**amountCents** | **Integer** | Always positive; direction is given by debit and credit. |  |
|**debit** | [**LedgerAccountSide**](LedgerAccountSide.md) |  |  |
|**credit** | [**LedgerAccountSide**](LedgerAccountSide.md) |  |  |
|**holdUntil** | **OffsetDateTime** |  |  |
|**releasedByEntryId** | **String** |  |  |
|**reversesEntryId** | **String** |  |  |
|**referenceType** | **String** |  |  |
|**referenceId** | **String** |  |  |
|**cause** | **String** |  |  |
|**externalReference** | **String** | The payout reference recorded with a settlement (your transfer or invoice id). |  |
|**actor** | **String** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| ACCRUAL | &quot;accrual&quot; |
| APPROVAL | &quot;approval&quot; |
| HOLD_RELEASE | &quot;hold_release&quot; |
| ADJUSTMENT | &quot;adjustment&quot; |
| SETTLING | &quot;settling&quot; |
| SETTLEMENT | &quot;settlement&quot; |
| REVERSAL | &quot;reversal&quot; |
| TOPUP | &quot;topup&quot; |
| TRANSFER | &quot;transfer&quot; |
| FEE | &quot;fee&quot; |



