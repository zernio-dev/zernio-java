

# CreatorCampaignCaps


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxParticipants** | **Integer** | Invites and joins past this count answer 403. |  [optional] |
|**maxSubmissionsPerParticipantPerDay** | **Integer** | Posts one participant can submit to this campaign per UTC day, counting every submission whatever its status. The next submit that day answers 409 invalid_resource_state. |  [optional] |
|**maxAccountsPerParticipant** | **Integer** | Accounts a participant can use in this campaign. Connecting a new account past it answers 400; only the first accounts connected, up to this count, can submit posts. |  [optional] |
|**authenticityThreshold** | **BigDecimal** | A submission whose authenticity score falls below this is flagged &#x60;low_authenticity&#x60;. It is never rejected automatically. Defaults to 40 on create. |  |



