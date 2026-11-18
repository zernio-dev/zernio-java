

# CreateCrmContactRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**phone** | **String** |  |  [optional] |
|**company** | **String** |  |  [optional] |
|**ownerId** | **String** | An id from &#x60;GET /v1/crm/{accountId}/owners&#x60;. |  [optional] |
|**properties** | [**Map&lt;String, CrmNativePropertiesValue&gt;**](CrmNativePropertiesValue.md) | Native fields by internal name (HubSpot &#x60;lifecyclestage&#x60;, Salesforce &#x60;LeadSource&#x60; or &#x60;Industry__c&#x60;). A unified field of the same request wins over its native twin. &#x60;null&#x60; clears a field. |  [optional] |
|**createAs** | [**CreateAsEnum**](#CreateAsEnum) | Salesforce only. Defaults to the connection&#39;s &#x60;createAs&#x60; setting. Ignored on HubSpot. |  [optional] |



## Enum: CreateAsEnum

| Name | Value |
|---- | -----|
| LEAD | &quot;lead&quot; |
| CONTACT | &quot;contact&quot; |



