

# CreatorPortalPayoutEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**amountCents** | **Integer** |  |  |
|**fromBucket** | **String** | The participant bucket the money left; null when it came from outside the participant. |  |
|**toBucket** | **String** | The participant bucket the money entered; null when it left the participant. |  |
|**holdUntil** | **OffsetDateTime** |  |  |
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



