

# ConnectSlackChannelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**channelId** | **String** | Slack channel id, C... or G.... Send this or channelIds, not both. |  [optional] |
|**channelIds** | **List&lt;String&gt;** | Several channels of the workspace to connect, each as its own account. With two or more distinct ids the response lists &#x60;accounts&#x60; and &#x60;failed&#x60; instead of &#x60;account&#x60;, and the request is refused with 400 on a reconnect. A single id behaves exactly like channelId. |  [optional] |
|**redirectUrl** | **String** | channelIds only: a URL to return in &#x60;redirect_url&#x60;, with &#x60;connected&#x60;, &#x60;profileId&#x60;, &#x60;accountId&#x60; and &#x60;accountIds&#x60; appended. |  [optional] |
|**pendingDataToken** | **String** | Nonce from the OAuth redirect. Required unless accountId is sent. |  [optional] |
|**accountId** | **String** | Existing Slack account whose workspace token is reused. Required unless pendingDataToken is sent. |  [optional] |



