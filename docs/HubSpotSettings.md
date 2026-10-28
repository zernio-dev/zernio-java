

# HubSpotSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Zernio account ID of the HubSpot connection. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**hubId** | **String** | HubSpot portal (hub) ID. |  |
|**hubDomain** | **String** | HubSpot portal domain, when HubSpot reports one. |  |
|**scopes** | **List&lt;String&gt;** | OAuth scopes the portal granted. |  |
|**syncContacts** | **Boolean** | Whether Zernio creates HubSpot contacts for inbox contacts that match none. |  |
|**logMessages** | **Boolean** | Whether Zernio logs inbox messages on HubSpot contact timelines. |  |
|**reportDeals** | **Boolean** | Whether Zernio sends closed-won deals as Purchase events to the profile&#39;s event destinations. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| HUBSPOT | &quot;hubspot&quot; |



