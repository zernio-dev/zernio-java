

# WebhookPayloadCampaignPayoutPayoutFailure

Present on campaign_payout.failed only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transferId** | **String** | The Zernio transfer that did not go through. |  |
|**amountCents** | **Integer** | The payout amount that did not reach the creator. It is returned to payable, minus any amount a rejection made while the payout was in flight claws back to the campaign budget; payableCents is the balance after both. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | returned: Stripe refused the transfer. stale: it could not be confirmed with Stripe within 24 hours. reversed: Stripe reversed it after it was sent; the settlement is undone. |  |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| RETURNED | &quot;returned&quot; |
| STALE | &quot;stale&quot; |
| REVERSED | &quot;reversed&quot; |



