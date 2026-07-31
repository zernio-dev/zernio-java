

# ConnectedApp

An OAuth client (AI assistant / MCP connector) authorized by the user and still holding at least one live token. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** |  |  [optional] |
|**clientName** | **String** | Name the client declared at registration. Registration is open, so this is self-declared and not verified. |  [optional] |
|**redirectHost** | **String** | Host of the client&#39;s registered redirect URI (non-http schemes are shown as scheme//host). The destination an impostor cannot fake. |  [optional] |
|**scopes** | **List&lt;String&gt;** | Scopes granted on the most recent token. |  [optional] |
|**authorizedAt** | **OffsetDateTime** |  |  [optional] |
|**lastUsedAt** | **OffsetDateTime** | Last time any of the client&#39;s live tokens authenticated a request. |  [optional] |
|**tokenCount** | **Integer** | Live tokens held by the client (an active session is typically one access plus one refresh token). |  [optional] |



