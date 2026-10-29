

# OAuthAppSlackEvents

Slack only; null on other platforms. Slack delivers messages and mentions to your app's own Request URL.  Save the app's signing secret first (`slackSigningSecret`), then set this Request URL under Event Subscriptions and subscribe the listed bot events. Zernio checks each delivery against that secret. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestUrl** | **URI** |  |  |
|**botEvents** | **List&lt;String&gt;** | Subscribe the app to these bot events. |  |



