

# UpdateOAuthAppRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**label** | **String** |  |  [optional] |
|**clientSecret** | **String** |  |  [optional] |
|**scopeAreas** | [**List&lt;ScopeAreasEnum&gt;**](#List&lt;ScopeAreasEnum&gt;) | Replaces the areas new connects request. Accounts already connected keep what they were granted until they reconnect. |  [optional] |



## Enum: List&lt;ScopeAreasEnum&gt;

| Name | Value |
|---- | -----|
| POSTING | &quot;posting&quot; |
| ANALYTICS | &quot;analytics&quot; |
| COMMENTS | &quot;comments&quot; |
| MESSAGING | &quot;messaging&quot; |



