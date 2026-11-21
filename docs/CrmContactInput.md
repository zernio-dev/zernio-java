

# CrmContactInput

Unified fields, mapped to HubSpot `firstname`, `lastname`, `email`, `phone`, `company`, `hubspot_owner_id`, Salesforce `FirstName`, `LastName`, `Email`, `Phone`, `Company` (Leads), `OwnerId` and GoHighLevel `firstName`, `lastName`, `email`, `phone`, `companyName`, `assignedTo`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**phone** | **String** |  |  [optional] |
|**company** | **String** |  |  [optional] |
|**ownerId** | **String** | An id from &#x60;GET /v1/crm/{accountId}/owners&#x60;. |  [optional] |
|**properties** | [**Map&lt;String, CrmNativePropertiesValue&gt;**](CrmNativePropertiesValue.md) | Native fields by internal name (HubSpot &#x60;lifecyclestage&#x60;, Salesforce &#x60;LeadSource&#x60; or &#x60;Industry__c&#x60;). On GoHighLevel, a record field (&#x60;source&#x60;, an opportunity &#x60;status&#x60;) or else a custom field id or key. A unified field of the same request wins over its native twin. &#x60;null&#x60; clears a field. |  [optional] |



