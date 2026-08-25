

# ConnectSlackChannelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**channelId** | **String** | Slack channel id, C... or G... |  |
|**pendingDataToken** | **String** | Nonce from the OAuth redirect. Required unless accountId is sent. |  [optional] |
|**accountId** | **String** | Existing Slack account whose workspace token is reused. Required unless pendingDataToken is sent. |  [optional] |



