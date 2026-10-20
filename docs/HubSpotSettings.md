

# HubSpotSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Zernio account ID of the HubSpot connection. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**hubId** | **String** | HubSpot portal (hub) ID. |  |
|**hubDomain** | **String** | HubSpot portal domain, when HubSpot reports one. |  |
|**scopes** | **List&lt;String&gt;** | OAuth scopes the portal granted. |  |
|**syncContacts** | **Boolean** | Whether Zernio creates or updates HubSpot contacts for inbox contacts. |  |
|**logMessages** | **Boolean** | Whether Zernio logs inbox messages on HubSpot contact timelines. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| HUBSPOT | &quot;hubspot&quot; |



