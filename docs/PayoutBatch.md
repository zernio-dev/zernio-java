

# PayoutBatch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**campaignId** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;awaiting_payment&#x60; until the card payment completes; &#x60;paying&#x60; while transfers go out; then &#x60;paid&#x60;, &#x60;partially_failed&#x60; (some items failed or were skipped), &#x60;failed&#x60; (none paid) or &#x60;expired&#x60; (the Checkout expired unpaid, every amount is payable again). |  |
|**method** | [**MethodEnum**](#MethodEnum) |  |  |
|**amountCents** | **Integer** | Total the creators receive. |  |
|**feeCents** | **Integer** | Total Zernio fee. |  |
|**totalCents** | **Integer** | The card charge: amountCents plus feeCents. |  |
|**items** | [**List&lt;PayoutBatchItem&gt;**](PayoutBatchItem.md) |  |  |
|**paidAt** | **OffsetDateTime** |  |  |
|**finishedAt** | **OffsetDateTime** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AWAITING_PAYMENT | &quot;awaiting_payment&quot; |
| PAYING | &quot;paying&quot; |
| PAID | &quot;paid&quot; |
| PARTIALLY_FAILED | &quot;partially_failed&quot; |
| FAILED | &quot;failed&quot; |
| EXPIRED | &quot;expired&quot; |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| CARD | &quot;card&quot; |



