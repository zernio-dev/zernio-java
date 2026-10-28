

# CampaignSettlement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entryId** | **String** | The ledger settlement entry. |  |
|**participantId** | **String** |  |  |
|**amountCents** | **Integer** |  |  |
|**externalReference** | **String** |  |  |
|**payableCents** | **Integer** | Payable balance left after this settlement. |  |
|**settledAt** | **OffsetDateTime** |  |  |
|**transferId** | **String** | Treasury settlement only: the Zernio transfer that moved the money. The creator receives amountCents in full. |  [optional] |
|**feeCents** | **Integer** | Treasury settlement only: the transfer fee, added on top of amountCents. |  [optional] |
|**totalCents** | **Integer** | Treasury settlement only: debited from your balance, amountCents plus feeCents. |  [optional] |



