

# OAuthApp


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Pass it as &#x60;oauthAppId&#x60; on GET /v1/connect/{platform} to connect through this app. |  |
|**platform** | **String** | The platform the app belongs to, as in GET /v1/connect/{platform}. |  |
|**label** | **String** |  |  |
|**clientId** | **String** | The client ID (or app ID) of your app on the platform. The secret is never returned. |  |
|**scopeAreas** | [**List&lt;ScopeAreasEnum&gt;**](#List&lt;ScopeAreasEnum&gt;) | The permission areas every connect through this app requests. Pick only what your app is approved for on the platform. |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;ok&#x60;: the platform accepted the keys at the last check. &#x60;unchecked&#x60;: the check could not reach a verdict (see lastError). &#x60;invalid&#x60;: the platform rejected the keys; connects and token refreshes through this app will fail until the secret is rotated. |  |
|**lastCheckedAt** | **OffsetDateTime** |  |  [optional] |
|**lastError** | **String** |  |  [optional] |
|**accountCount** | **Integer** | Connected accounts currently running on this app. |  |
|**redirectUri** | **URI** | The OAuth redirect URI to allow in your app&#39;s settings on the platform. |  |
|**webhook** | [**OAuthAppWebhook**](OAuthAppWebhook.md) |  |  [optional] |
|**sharedWebhookUrl** | **URI** | TikTok only: set this as the webhook callback URL in your TikTok developer app. TikTok uses it to report when a video finishes publishing; Zernio also checks the publish status itself, so posting works without it. Null on other platforms. |  [optional] |
|**hasSlackSigningSecret** | **Boolean** | Slack only: whether the signing secret of your Slack app is saved. Without it Zernio refuses every event sent to &#x60;slackEvents.requestUrl&#x60;. |  [optional] |
|**slackEvents** | [**OAuthAppSlackEvents**](OAuthAppSlackEvents.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: List&lt;ScopeAreasEnum&gt;

| Name | Value |
|---- | -----|
| POSTING | &quot;posting&quot; |
| ANALYTICS | &quot;analytics&quot; |
| COMMENTS | &quot;comments&quot; |
| MESSAGING | &quot;messaging&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;ok&quot; |
| UNCHECKED | &quot;unchecked&quot; |
| INVALID | &quot;invalid&quot; |



