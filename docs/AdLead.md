

# AdLead


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Zernio lead id. |  [optional] |
|**leadgenId** | **String** | Meta lead id. On LinkedIn, the leadFormResponse id. |  [optional] |
|**formId** | **String** |  |  [optional] |
|**formName** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**adId** | **String** |  |  [optional] |
|**adsetId** | **String** |  |  [optional] |
|**campaignId** | **String** | On LinkedIn, this is the LinkedIn Campaign id, which corresponds to platformAdSetId on GET /v1/ads (LinkedIn&#39;s Campaign Group is Zernio&#39;s campaign). |  [optional] |
|**isOrganic** | **Boolean** |  |  [optional] |
|**createdTime** | **String** | ISO 8601. |  [optional] |
|**fields** | **Map&lt;String, String&gt;** | Question key → answer. On LinkedIn, the key is the lowercased predefinedField, else the question name, else the numeric questionId; multiple-choice values are option labels (unlike Meta, which returns the option key). |  [optional] |
|**fieldData** | **List&lt;Object&gt;** | Raw Meta field_data. |  [optional] |
|**consents** | [**List&lt;AdLeadConsent&gt;**](AdLeadConsent.md) | Meta lead forms only: the answer to every custom disclaimer checkbox, required or optional. Empty when the form has none, and may be empty on leads stored before 2026-10-22. LinkedIn leads do not carry the field. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Meta leads only. &#x60;contacted&#x60; is set when the first WhatsApp message of a lead_received workflow is delivered, &#x60;unreachable&#x60; when it fails or the phone number is not valid. |  [optional] |
|**statusChangedAt** | **OffsetDateTime** |  |  [optional] |
|**value** | **BigDecimal** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**contactId** | **String** | The contact a lead_received workflow created or matched for this lead. |  [optional] |
|**firstContactedAt** | **OffsetDateTime** | When the first WhatsApp message to the lead was delivered. |  [optional] |
|**conversationId** | **String** | The Inbox conversation a lead_received workflow opened with the lead. |  [optional] |
|**webhookDeliveredAt** | **OffsetDateTime** | Meta leads only. When the &#x60;lead.received&#x60; webhook was delivered; null while it has not been. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;new&quot; |
| CONTACTED | &quot;contacted&quot; |
| UNREACHABLE | &quot;unreachable&quot; |
| QUALIFIED | &quot;qualified&quot; |
| CONVERTED | &quot;converted&quot; |
| DISQUALIFIED | &quot;disqualified&quot; |



