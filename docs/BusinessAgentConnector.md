

# BusinessAgentConnector


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Unique per number. |  |
|**description** | **String** | Tell the agent what the service provides. |  [optional] |
|**baseUrl** | **URI** | Public HTTPS URL reachable from Meta. |  |
|**connectorProtocol** | **String** |  |  [optional] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) |  |  |
|**authConfig** | [**BusinessAgentConnectorInputAuthConfig**](BusinessAgentConnectorInputAuthConfig.md) |  |  [optional] |
|**userAuthInjectionConfig** | [**BusinessAgentConnectorInputUserAuthInjectionConfig**](BusinessAgentConnectorInputUserAuthInjectionConfig.md) |  |  [optional] |
|**requiresCertificate** | **Boolean** |  |  [optional] |
|**id** | **String** |  |  |
|**mcpToolSync** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**mtlsConfig** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**connectionStatus** | [**BusinessAgentConnectorAllOfConnectionStatus**](BusinessAgentConnectorAllOfConnectionStatus.md) |  |  [optional] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| OAUTH2_CLIENT_CREDENTIALS | &quot;OAUTH2_CLIENT_CREDENTIALS&quot; |
| API_KEY | &quot;API_KEY&quot; |
| NONE | &quot;NONE&quot; |



