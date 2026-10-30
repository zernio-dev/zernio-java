

# CreateOAuthAppRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** | One of the platforms listed in &#x60;platforms&#x60; of GET /v1/connect/oauth-apps. |  |
|**label** | **String** |  |  |
|**clientId** | **String** |  |  |
|**clientSecret** | **String** |  |  |
|**metaAppId** | **String** | Instagram only: the numeric ID of the Meta app your Instagram app lives in. Zernio uses it with &#x60;metaAppSecret&#x60; to register the webhook. Send both or neither. |  [optional] |
|**metaAppSecret** | **String** | Instagram only: the secret of that Meta app. Never returned. |  [optional] |
|**slackSigningSecret** | **String** | Slack only: the signing secret from the app&#39;s Basic Information page. Needed to receive events from your Slack app; any other platform is a 400. |  [optional] |
|**scopeAreas** | [**List&lt;ScopeAreasEnum&gt;**](#List&lt;ScopeAreasEnum&gt;) | Areas this app requests. Defaults to every area the platform supports; an area the platform cannot request separately is a 400. |  [optional] |



## Enum: List&lt;ScopeAreasEnum&gt;

| Name | Value |
|---- | -----|
| POSTING | &quot;posting&quot; |
| ANALYTICS | &quot;analytics&quot; |
| COMMENTS | &quot;comments&quot; |
| MESSAGING | &quot;messaging&quot; |



