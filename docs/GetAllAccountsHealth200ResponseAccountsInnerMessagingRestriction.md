

# GetAllAccountsHealth200ResponseAccountsInnerMessagingRestriction

Observed from Meta's own error subcodes on our own sends (2534122, 1893063, 2534029), not a live probe. Set on the first refused send and cleared when a later send succeeds, so it lags reality by one send in each direction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**subcode** | **Integer** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**firstSeenAt** | **OffsetDateTime** |  |  [optional] |
|**lastSeenAt** | **OffsetDateTime** |  |  [optional] |



