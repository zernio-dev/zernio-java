

# BusinessAgentConnector

Secret values are never returned: auth_config and mtls_config leave out client_secret, client_key, private_key and every API key value. Send them again with the credentials call to rotate them.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**baseUrl** | **URI** |  |  |
|**connectorProtocol** | **String** |  |  [optional] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) |  |  |
|**authConfig** | **Map&lt;String, Object&gt;** | What Meta stores for the connector&#39;s auth (for example oauth2_client_credentials with token_url and client_id), without secret values. |  [optional] |
|**userAuthInjectionConfig** | [**BusinessAgentConnectorUserAuthInjectionConfig**](BusinessAgentConnectorUserAuthInjectionConfig.md) |  |  [optional] |
|**requiresCertificate** | **Boolean** |  |  [optional] |
|**mcpToolSync** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**mtlsConfig** | **Map&lt;String, Object&gt;** | Certificate details, without client_key or private_key. |  [optional] |
|**connectionStatus** | [**BusinessAgentConnectorConnectionStatus**](BusinessAgentConnectorConnectionStatus.md) |  |  [optional] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| OAUTH2_CLIENT_CREDENTIALS | &quot;OAUTH2_CLIENT_CREDENTIALS&quot; |
| API_KEY | &quot;API_KEY&quot; |
| NONE | &quot;NONE&quot; |



