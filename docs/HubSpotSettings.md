

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
|**logDeliveryStatus** | **Boolean** | Whether Zernio keeps the delivery status (sent, delivered, read, played, failed) of logged outgoing messages up to date on their HubSpot timeline entries. Only applies while &#x60;logMessages&#x60; is on. Defaults to &#x60;true&#x60;. |  |
|**contactDefaults** | **Map&lt;String, String&gt;** | Values Zernio sets on contacts it creates, keyed by HubSpot internal property name, for properties the portal requires on create (for example &#x60;lifecyclestage: lead&#x60;). The contact&#39;s own name, email and phone win. Empty object when none. |  |
|**syncIssue** | [**HubSpotSettingsSyncIssue**](HubSpotSettingsSyncIssue.md) |  |  |
|**reportDeals** | **Boolean** | Whether Zernio sends closed-won deals as Purchase events to the profile&#39;s event destinations. |  |
|**useDealsAsResults** | **Boolean** | Whether closed-won deals count as sales on the ad campaign that brought their contact, in campaign results and ad rules. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| HUBSPOT | &quot;hubspot&quot; |



