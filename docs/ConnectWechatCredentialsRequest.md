

# ConnectWechatCredentialsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | The Official Account&#39;s AppID (starts with wx). |  |
|**appSecret** | **String** | The Official Account&#39;s AppSecret (32 characters). |  |
|**state** | **String** | Required state formatted as {userId}-{profileId}. Get userId from GET /v1/users and profileId from GET /v1/profiles. |  |
|**displayName** | **String** | Name to show for the account. Defaults to \&quot;WeChat Official Account\&quot;. |  [optional] |
|**redirectUrl** | **URI** | Optional URL to redirect to after a successful connection. |  [optional] |



