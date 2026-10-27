

# ListFormLeads200ResponseLeadsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Meta leadgenId. |  [optional] |
|**leadId** | **String** | Zernio lead id, for PATCH /v1/ads/leads/{id}. Only on persisted leads. |  [optional] |
|**status** | **String** | Lead status (see PATCH /v1/ads/leads/{id}). Only on persisted leads. |  [optional] |
|**createdTime** | **String** |  |  [optional] |
|**adId** | **String** |  |  [optional] |
|**formId** | **String** |  |  [optional] |
|**fields** | **Map&lt;String, String&gt;** |  |  [optional] |
|**fieldData** | **List&lt;Object&gt;** |  |  [optional] |
|**consents** | [**List&lt;AdLeadConsent&gt;**](AdLeadConsent.md) | Meta lead forms only: the answer to every custom disclaimer checkbox, required or optional. Empty when the form has none, and may be empty on leads stored before 2026-10-22. LinkedIn leads do not carry the field. |  [optional] |



