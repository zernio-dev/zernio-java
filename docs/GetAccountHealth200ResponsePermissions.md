

# GetAccountHealth200ResponsePermissions


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**posting** | [**List&lt;GetAccountHealth200ResponsePermissionsPostingInner&gt;**](GetAccountHealth200ResponsePermissionsPostingInner.md) |  |  [optional] |
|**analytics** | [**List&lt;GetAccountHealth200ResponsePermissionsPostingInner&gt;**](GetAccountHealth200ResponsePermissionsPostingInner.md) |  |  [optional] |
|**optional** | [**List&lt;GetAccountHealth200ResponsePermissionsPostingInner&gt;**](GetAccountHealth200ResponsePermissionsPostingInner.md) |  |  [optional] |
|**canPost** | **Boolean** | Whether the granted OAuth scopes allow posting. Scopes only: for WhatsApp, whether Meta lets the number send is &#x60;platformConnection.phoneStatus&#x60; and the overall &#x60;status&#x60;. |  [optional] |
|**canFetchAnalytics** | **Boolean** |  |  [optional] |
|**missingRequired** | **List&lt;String&gt;** |  |  [optional] |
|**scopeAreas** | [**Map&lt;String, InnerEnum&gt;**](#Map&lt;String, InnerEnum&gt;) | Present when the account connected with &#x60;scopes&#x60; or through your own OAuth app: each permission area the platform splits, as granted, missing or not_requested. An area never requested does not make the account unhealthy. |  [optional] |



## Enum: Map&lt;String, InnerEnum&gt;

| Name | Value |
|---- | -----|
| GRANTED | &quot;granted&quot; |
| MISSING | &quot;missing&quot; |
| NOT_REQUESTED | &quot;not_requested&quot; |



