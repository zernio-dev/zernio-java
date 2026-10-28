

# UpdateHubSpotSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**syncContacts** | **Boolean** | Create a HubSpot contact for an inbox contact that matches none by email or phone. A match is linked as it is and never updated. |  [optional] |
|**logMessages** | **Boolean** | Log inbound and outbound inbox messages on the contact&#39;s HubSpot timeline. |  [optional] |
|**reportDeals** | **Boolean** | Send each deal that becomes closed won as a Purchase to the profile&#39;s event destinations, about once an hour. Requires the portal to have granted &#x60;crm.objects.deals.read&#x60;; otherwise 400. Deals closed before it was turned on are not sent. |  [optional] |



