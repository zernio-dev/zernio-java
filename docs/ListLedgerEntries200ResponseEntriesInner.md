

# ListLedgerEntries200ResponseEntriesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) |  |  [optional] |
|**amountCents** | **Integer** | Always positive; direction is given by debit and credit |  [optional] |
|**debit** | [**LedgerAccountSide**](LedgerAccountSide.md) |  |  [optional] |
|**credit** | [**LedgerAccountSide**](LedgerAccountSide.md) |  |  [optional] |
|**holdUntil** | **OffsetDateTime** |  |  [optional] |
|**releasedByEntryId** | **String** |  |  [optional] |
|**referenceType** | **String** |  |  [optional] |
|**referenceId** | **String** |  |  [optional] |
|**reversesEntryId** | **String** |  |  [optional] |
|**cause** | **String** |  |  [optional] |
|**actor** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



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



