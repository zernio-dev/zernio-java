

# ConnectLineCredentialsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelId** | **String** | The Messaging API channel&#39;s Channel ID (digits only). |  |
|**channelSecret** | **String** | The Messaging API channel&#39;s Channel secret (32 hex characters). |  |
|**state** | **String** | Required state formatted as {userId}-{profileId}. Get userId from GET /v1/users and profileId from GET /v1/profiles. |  |
|**redirectUrl** | **URI** | Optional URL to redirect to after a successful connection. |  [optional] |



