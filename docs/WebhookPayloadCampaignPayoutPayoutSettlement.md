

# WebhookPayloadCampaignPayoutPayoutSettlement

Present on campaign_payout.settled only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entryId** | **String** | The ledger settlement entry. |  |
|**amountCents** | **Integer** |  |  |
|**externalReference** | **String** |  |  |
|**recorded** | **Boolean** | True when the payout was made outside Zernio and only recorded here; false when Zernio moved the money through the treasury. |  |
|**transferId** | **String** | Treasury settlement only: the Zernio transfer that moved the money. The creator receives amountCents in full. |  [optional] |
|**feeCents** | **Integer** | Treasury settlement only: the transfer fee, added on top of amountCents. |  [optional] |
|**totalCents** | **Integer** | Treasury settlement only: debited from your balance, amountCents plus feeCents. |  [optional] |



