

# SettleCampaignParticipantRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountCents** | **Integer** | Defaults to the whole payable balance. |  [optional] |
|**externalReference** | **String** | Your payout id. Required when the campaign settles externally. |  [optional] |
|**recordOnly** | **Boolean** | Treasury campaigns only, and required there: record a payout you already made outside Zernio. Ignored on other settlement modes, which always record. |  [optional] |



