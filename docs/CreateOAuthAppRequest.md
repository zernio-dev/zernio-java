

# CreateOAuthAppRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** | One of the platforms listed in &#x60;platforms&#x60; of GET /v1/connect/oauth-apps. |  |
|**label** | **String** |  |  |
|**clientId** | **String** |  |  |
|**clientSecret** | **String** |  |  |
|**scopeAreas** | [**List&lt;ScopeAreasEnum&gt;**](#List&lt;ScopeAreasEnum&gt;) | Areas this app requests. Defaults to every area the platform supports; an area the platform cannot request separately is a 400. |  [optional] |



## Enum: List&lt;ScopeAreasEnum&gt;

| Name | Value |
|---- | -----|
| POSTING | &quot;posting&quot; |
| ANALYTICS | &quot;analytics&quot; |
| COMMENTS | &quot;comments&quot; |
| MESSAGING | &quot;messaging&quot; |
| ADS | &quot;ads&quot; |



